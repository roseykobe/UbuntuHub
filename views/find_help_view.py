import flet as ft
from business_logic import fhchat
#from business_logic.offers import Offers
from business_logic.offers import Offers


def find_help(page: ft.Page, fhchat: fhchat, offers: Offers):

    def confirm_delete(info):
        def yes(e):
            if state["tab"]=="paid":
                offers.delete_paid_offer(info["offer_id"])
                page.pop_dialog()
                render()
            else:
                offers.delete_free_offer(info["offer_id"])
                page.pop_dialog()
                render()

            page.show_dialog(ft.SnackBar(
                ft.Text("offer deleted"),
                duration= 1500,
                behavior=ft.SnackBarBehavior.FLOATING,
                margin= ft.Margin.only(bottom= 100, left= 20, right= 20),
            ))
            page.update()
        def no(e):
            page.pop_dialog()

        page.show_dialog(
            ft.AlertDialog(
                modal= True,
                title= ft.Text("Delete this offer?"),
                content= ft.Text(info["title"]),
                actions= [
                    ft.TextButton("Cancel", on_click= no),
                    ft.TextButton(
                        "Delete", on_click=yes, 
                        style= ft.ButtonStyle(color= ft.Colors.RED),
                    ),

                ],
            )
        )

    # Remembers which tab is open and what was typed
    state = {"tab": "paid", "query": ""}

    def clicked(e):
        info= e.control.data
        if info["helper_id"] == 65:
            confirm_delete(info)
        else:
            fhchat.to_chat(e.control.data)

    # ---------- One neat card per offer ----------
    def make_item(offer, color):
        helper = offers.users[offer["helper_id"]]
        name = helper["name"]
        

        demo_user= offer["helper_id"] == 65
        

        # Name + verified badge (badge only shows when verified is True)
        name_row = [ft.Text(name, size=15, weight=ft.FontWeight.W_600)]
        if helper.get("verified"):
            name_row.append(
                ft.Icon(icon=ft.Icons.VERIFIED, color=ft.Colors.BLUE, size=16)
            )

        rating, count= offers.get_rating(offer["helper_id"])
        if count==0:
            #name_row.append(ft.Text("New", size= 12, color= ft.Colors.GREY_600))
            rating_ctrl= ft.Text("New", size= 12, color= ft.Colors.GREY_600)
        else:
            rating_ctrl= ft.Row(
                [ft.Icon(icon= ft.Icons.STAR, color= ft.Colors.AMBER, size= 16),
                ft.Text(f'{rating:.1f} ({count})', size= 12, color= ft.Colors.GREY_400)
                ], spacing= 2, tight=True
                )
            

        # The offer (title already includes the price) + optional mentorship badge
        details = [ft.Text(offer["title"], size=13)]
        if offer.get("mentorship"):
            details.append(
                ft.Container(
                    padding=ft.Padding(left=8, right=8, top=2, bottom=2),
                    border_radius=10,
                    bgcolor=ft.Colors.ORANGE_100,
                    content=ft.Row(
                        spacing=4,
                        tight=True,
                        controls=[
                            ft.Icon(icon=ft.Icons.FAVORITE, color=ft.Colors.ORANGE, size=12),
                            ft.Text("offers mentorship", size=11, color=ft.Colors.ORANGE_700),
                        ],
                    ),
                )
            )

        return ft.GestureDetector(
            on_tap=clicked,
            #data=f"{name} - {offer['title']}",
            data= {
                "helper_id": offer["helper_id"],
                "name": name,
                "title": offer["title"],
                "verified": bool(helper.get("verified")),
                "offer_id": offer['offer_id'],
                "helper_id": offer["helper_id"]
            },
            content=ft.Container(
                bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.ON_SURFACE),
                border_radius=12,
                margin=ft.Margin.only(left=8, right=8, bottom=6),
                content=ft.ListTile(
                    leading=ft.CircleAvatar(
                        radius=20,
                        bgcolor=color,
                        content=ft.Text(
                            name[0].upper(),
                            color=ft.Colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ),
                    #title=ft.Row(controls=name_row, spacing=6, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                    title= ft.Row(
                        controls= [
                            ft.Row(controls= name_row, spacing= 4, expand= True),
                            rating_ctrl
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    subtitle=ft.Column(controls=details, spacing=4, tight=True),
                    trailing=ft.Icon(icon= ft.Icons.DELETE_OUTLINE if demo_user else ft.Icons.CHEVRON_RIGHT, color=ft.Colors.RED_300 if demo_user else ft.Colors.GREY_500),
                ),
            ),
        )

    # groups = list of (category_dict, [offers])
    def make_list(groups, expand_all=False):
        # Nothing matched the search
        if not groups:
            return ft.Container(
                padding=30,
                content=ft.Text(
                    "No results found",
                    size=14,
                    color=ft.Colors.GREY_600,
                    text_align=ft.TextAlign.CENTER,
                ),
            )

        return ft.Column(
            controls=[
                ft.ExpansionTile(
                    expanded=expand_all,
                    title=ft.Row(
                        controls=[
                            ft.Icon(icon=cat["icon"], size=18, color=cat["color"]),
                            ft.Text(
                                f"  {cat['name']}",
                                size=16,
                                weight=ft.FontWeight.W_500,
                            ),
                        ],
                        spacing=4,
                    ),
                    controls=[make_item(o, cat["color"]) for o in items],
                )
                for cat, items in groups
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    # Collects the offers of the open tab, grouped by category
    def get_groups():
        if state["tab"] == "paid":
            categories = offers.paid_categories
            get_offers = offers.get_paid_offers
        else:
            # Free items/services aren't in the new offers file yet
            #categories = getattr(offers, "free_categories", {})
            #get_offers = getattr(offers, "get_free_offers", lambda category: [])
            categories= offers.free_categories
            get_offers= offers.get_free_offers


        groups = []
        for key, cat in categories.items():
            # Skip offers whose helper doesn't exist in offers.users
            items = [o for o in get_offers(key) if o["helper_id"] in offers.users]
            if items:
                groups.append((cat, items))
        return groups

    # Keeps only the categories/offers that match what was typed
    def filter_groups(groups, q):
        if not q:
            return groups

        result = []
        for cat, items in groups:
            if q in cat["name"].lower():
                # Category name matches, so keep all its offers
                result.append((cat, items))
            else:
                matches = [
                    o for o in items
                    if q in o["title"].lower()
                    or q in offers.users[o["helper_id"]]["name"].lower()
                ]
                if matches:
                    result.append((cat, matches))
        return result

    # Holds whichever list is active
    body = ft.Container(expand=True)

    # Rebuilds the list for the current tab + search text
    def render():
        q = state["query"].strip().lower()
        body.content = make_list(filter_groups(get_groups(), q), expand_all=bool(q))

    def show_list(e):
        if e.control.data == "one":
            state["tab"] = "paid"
            btn_one.bgcolor = ft.Colors.ORANGE
            btn_one.color = ft.Colors.WHITE
            btn_two.bgcolor = ft.Colors.ORANGE_100
            btn_two.color = None
        else:
            state["tab"] = "free"
            btn_two.bgcolor = ft.Colors.ORANGE
            btn_two.color = ft.Colors.WHITE
            btn_one.bgcolor = ft.Colors.ORANGE_100
            btn_one.color = None
        render()
        page.update()

    def on_search(e):
        state["query"] = search_field.value or ""
        render()
        page.update()

    btn_one = ft.FilledButton(
        "Help for Hire",
        data="one",
        on_click=show_list,
        bgcolor=ft.Colors.ORANGE,
        color=ft.Colors.WHITE,
        width=172,
    )

    btn_two = ft.FilledButton(
        "Free items/services",
        data="two",
        on_click=show_list,
        bgcolor=ft.Colors.ORANGE_100,
        width=172,
    )

    search_field = ft.TextField(
        hint_text="search category, name or skill",
        border=ft.InputBorder.NONE,
        filled=True,
        bgcolor=ft.Colors.SURFACE,
        content_padding=10,
        text_size=14,
        width=300,
        text_align=ft.TextAlign.CENTER,
        on_change=on_search,
        on_submit=on_search,
    )

    # First draw (paid list, no search)
    render()

    return ft.View(
        route="/FindHelp",
        controls=[
            ft.AppBar(
                title=search_field,
                center_title=True,
                actions=[
                    ft.IconButton(
                        icon=ft.Icons.SEARCH,
                        tooltip="search",
                        icon_color=ft.Colors.BLUE,
                        on_click=on_search,
                    )
                ],
            ),
            ft.Row(
                spacing=25,
                controls=[btn_one, btn_two],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            body,
        ],
    )