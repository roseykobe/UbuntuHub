import flet as ft
from business_logic.offers import Offers
#from new.offers import Offers




def get_paid (page: ft.Page, offers: Offers):

    def on_checkbox_change(e):
        is_ticked= e.control.value
        print(is_ticked)

    mentorship= ft.Checkbox(label= "offer mentorship", value = False, on_change= on_checkbox_change)

    

    def check_field(e):
        post_btn_p.disabled= not paid_offer.value.strip()
        page.update()

    def post_offer(e):
        content= paid_offer.value.strip()
        print(content, "content")

        if not content:
            return

        is_ticked= mentorship.value
        category= e.control.namedata
        offers.add_paid_offer(content, category, is_ticked)
        paid_offer.value= ""
        post_btn_p.disabled= True
        mentorship.value= False
        page.pop_dialog()

        page.show_dialog(
                     ft.SnackBar(
                          ft.Text("success."),
                          duration= 2000,
                          behavior= ft.SnackBarBehavior.FLOATING,
                          margin= ft.Margin.only(bottom= 100, left=20, right= 20),
                     )
                )

        page.update()


    paid_offer= ft.TextField(hint_text= "write offer & price", filled= True, on_change= check_field)
    post_btn_p=ft.Button("Publish", bgcolor= ft.Colors.ORANGE, on_click= post_offer, disabled= True)


    def show_paid_popup(name):
        
        post_btn_p.namedata= name
        def close_popup(e):
            page.pop_dialog()

        def on_confirm(e):
            page.pop_dialog()

        dialog = ft.AlertDialog(
            modal=True,
            shape=ft.RoundedRectangleBorder(radius=16),
            title=ft.Row(
                spacing=12,
                controls=[
                    ft.Text(name, size=16, weight=ft.FontWeight.W_600, expand=True,  ),
                    ft.IconButton(icon= ft.Icons.CLOSE, icon_size= 20, on_click= close_popup),
                ],
            ),
            content=ft.Column(
                tight= True,
                spacing= 10,
                controls=[
                ft.Text("Describe your offer"),
                paid_offer,
                #ft.Checkbox(label= "want to mentor someone on this?", value = False, )
                mentorship,
                ]),

            actions=[
                post_btn_p,
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.show_dialog(dialog)

    def check_field1(e):
        post_btn_f.disabled= not free_offer.value.strip()
        page.update()
    
    def post_offer1(e):
        content= free_offer.value.strip()
        
    
        if not content:
            return
        
        is_ticked= mentorship.value
        category= e.control.data
        
        offers.add_free_offer(content, category, is_ticked)
        free_offer.value= ""
        post_btn_f.disabled= True
        mentorship.value= False
        page.pop_dialog()
        
        page.show_dialog(
                             ft.SnackBar(
                                  ft.Text("success."),
                                  duration= 2000,
                                  behavior= ft.SnackBarBehavior.FLOATING,
                                  margin= ft.Margin.only(bottom= 100, left=20, right= 20),
                             )
                        )
    
        page.update()

    #mentorship= ft.Checkbox(label= "want to mentor someone on this?", value = False, )
    free_offer= ft.TextField(hint_text= "write offer", filled= True, on_change= check_field1)
    post_btn_f=ft.Button("Publish", bgcolor= ft.Colors.ORANGE, on_click= post_offer1, data= mentorship.value, disabled= True)
    #mentorship= ft.Checkbox(label= "want to mentor someone on this?", value = False, )

    def show_free_popup(name):

        post_btn_f.data= name

    
        def close_popup(e):
            page.pop_dialog()
    
        def on_confirm(e):
            
            page.pop_dialog()
    
    
        dialog = ft.AlertDialog(
                modal=True,
                shape=ft.RoundedRectangleBorder(radius=16),
                title=ft.Row(
                    spacing=12,
                    controls=[
                        ft.Text(name, size=16, weight=ft.FontWeight.W_600, expand=True, ),
                        ft.IconButton(icon= ft.Icons.CLOSE, icon_size= 20, on_click= close_popup),
                    ],
                ),
                content=ft.Column(
                    tight= True,
                    spacing= 10,
                    controls=[
                    ft.Text("Describe your offer"),
                    #ft.TextField(hint_text= "e.g. ladies' boots, size 5", filled= True, read_only= True),
                    free_offer,
                    mentorship
                    ]),
    
                actions=[
                    post_btn_f,
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
    
        page.show_dialog(dialog)

        


    def on_item_tap(name, type):
        if type== "p":
            show_paid_popup(name)
        else:
            show_free_popup(name)

    
    def make_item(icon, icon_color, name, type):
        return ft.GestureDetector(
            on_tap=lambda e: on_item_tap(name, type),
            content=ft.Container(
                margin=ft.Margin.only(left=12, right=12, bottom=8),
                padding=ft.Padding.symmetric(horizontal=12, vertical=10),
                border_radius=10,
                bgcolor=ft.Colors.with_opacity(0.6, ft.Colors.WHITE),
                content=ft.Row(
                    spacing=12,
                    controls=[
                        ft.Icon(icon, size=20, color=icon_color),
                        ft.Text(name, size=14, color= ft.Colors.GREY_800, expand=True),
                        ft.Icon(
                            ft.Icons.CHEVRON_RIGHT,
                            size=18,
                            color=ft.Colors.GREY_500,
                        ),
                    ],
                ),
            ),
        )

    
    def make_tile(icon, color, title, subt, items, expanded=False):
        return ft.Container(
            margin=ft.Margin.symmetric(horizontal=12, vertical=6),
            border_radius=16,
            bgcolor=ft.Colors.with_opacity(0.10, color),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.30, color)),
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            content=ft.ExpansionTile(
                expanded=expanded,
                on_change=lambda e: on_tile_toggle(e, title),
                bgcolor=ft.Colors.TRANSPARENT,
                collapsed_bgcolor=ft.Colors.TRANSPARENT,
                title=ft.Row(
                    spacing=12,
                    controls=[
                        ft.Container(
                            content=ft.Icon(icon, size=20, color=ft.Colors.WHITE),
                            bgcolor=color,
                            padding=10,
                            border_radius=24,
                        ),
                        ft.Text(title, size=17, weight=ft.FontWeight.W_600),
                    ],
                ),
                subtitle=ft.Text(
                    f"{subt} ",
                    size=12,
                    color=ft.Colors.GREY_700,
                ),
                controls=[make_item(i, c, n, t) for i, c, n, t in items],
            ),
        )

    
    paid_services = [
        (ft.Icons.BOOK, ft.Colors.RED, "Tutoring", "p"),
        (ft.Icons.CONTENT_CUT, ft.Colors.ORANGE, "Hair & Grooming", "p"),
        (ft.Icons.HANDYMAN, ft.Colors.GREY, "Tools for Hire", "p"),
        (ft.Icons.SPA, ft.Colors.GREEN, "Gardening", "p"),
        (ft.Icons.LOCAL_LAUNDRY_SERVICE, ft.Colors.BLUE_GREY, "Laundry", "p"),
        (ft.Icons.ECO, ft.Colors.GREEN_800, "Veggies", "p"),
        (ft.Icons.LOCAL_CAFE, ft.Colors.ORANGE_300, "Baked Goods", "p"),
        (ft.Icons.BUILD, ft.Colors.DEEP_ORANGE, "Repairs", "p"),
        (ft.Icons.BATTERY_CHARGING_FULL, ft.Colors.YELLOW_800, "Phone Charging", "p"),
        (ft.Icons.TEXTURE, ft.Colors.PINK_200, "Sewing & Repairs", "p"),
        (ft.Icons.DIRECTIONS_BIKE, ft.Colors.BLUE_600, "Rides & Delivery", "p"),
        (ft.Icons.DESCRIPTION, ft.Colors.INDIGO_400, "CV & Job Application", "p"),
        (ft.Icons.CAMERA_ALT, ft.Colors.DEEP_PURPLE_300, "Photography", "p"),
        (ft.Icons.DEVICES, ft.Colors.BLUE_400, "Tech Help", "p"),
        (ft.Icons.CLEANING_SERVICES, ft.Colors.TEAL_400, "Cleaning", "p"),
        (ft.Icons.FACE, ft.Colors.ORANGE_300, "Makeup", "p"),
        (ft.Icons.BACK_HAND, ft.Colors.PINK_200, "Nails", "p"),
        (ft.Icons.MUSIC_NOTE, ft.Colors.PURPLE_300, "Music & Arts", "p"),
        (ft.Icons.HARDWARE, ft.Colors.GREY_500, "Welding", "p"),
    ]

    free_services = [
        (ft.Icons.CHECKROOM, ft.Colors.INDIGO_300, "Clothes", "f"),
        (ft.Icons.FOOD_BANK, ft.Colors.AMBER_800, "Food Pantry", "f"),
        (ft.Icons.BATHROOM, ft.Colors.CYAN_100, "Toiletries", "f"),
        (ft.Icons.BACKPACK, ft.Colors.BLUE_200, "School Supplies", "f"),
        (ft.Icons.HOME_REPAIR_SERVICE, ft.Colors.GREY_400, "Appliances", "f"),
        (ft.Icons.CHAIR, ft.Colors.BROWN_300, "Furniture", "f"),
        (ft.Icons.DEVICE_UNKNOWN, ft.Colors.PURPLE_300, "Electronics", "f"),
        (ft.Icons.BABY_CHANGING_STATION, ft.Colors.PINK_200, "Baby & Kids", "f"),
        (ft.Icons.SOUP_KITCHEN, ft.Colors.AMBER_600, "Baking & Cooking", "f"),
        (ft.Icons.DESCRIPTION, ft.Colors.INDIGO_400, "CV & Job Application", "f"),
        (ft.Icons.BOOK, ft.Colors.RED, "Tutoring", "f"),
        (ft.Icons.CAMERA_ALT, ft.Colors.DEEP_PURPLE_300, "Photography", "f"),
        (ft.Icons.CONTENT_CUT, ft.Colors.ORANGE, "Hair & Grooming", "f"),
        (ft.Icons.FACE, ft.Colors.DEEP_ORANGE_300, "Makeup", "f"),
        (ft.Icons.BACK_HAND, ft.Colors.PINK_200, "Nails", "f"),
        (ft.Icons.MUSIC_NOTE, ft.Colors.PURPLE_300, "Music & Arts", "f"),
    ]

    # ---------- Search: the two big tiles + what gets searched ----------
    tile_data = [
        (ft.Icons.WORK, ft.Colors.BLUE_50, "Offer Paid Services",
         "Get paid for your skills/products.", paid_services),
        (ft.Icons.HANDSHAKE, ft.Colors.ORANGE_200, "Offer for Free",
         "Give away items/services for free.", free_services),
    ]

    # "open" remembers which big tiles are expanded
    search_state = {"query": "", "open": set()}

    def build_tiles():
        q = search_state["query"].strip().lower()
        tiles = []
        for icon, color, title, subt, items in tile_data:
            # it[2] is the text on the list tile (e.g. "Tutoring")
            shown = [it for it in items if q in it[2].lower()]
            if not shown:
                continue
            tiles.append(
                make_tile(
                    icon, color, title, subt, shown,
                    expanded=bool(q) or title in search_state["open"],
                )
            )
        if not tiles:
            tiles.append(
                ft.Container(
                    padding=30,
                    content=ft.Text(
                        "No results found",
                        size=14,
                        color=ft.Colors.GREY_600,
                        text_align=ft.TextAlign.CENTER,
                    ),
                )
            )
        return tiles

    # Shows the search bar when a tile is open, hides it when all are closed
    def on_tile_toggle(e, title):
        if str(e.data).lower() == "true":
            search_state["open"].add(title)
        else:
            search_state["open"].discard(title)

        search_box.visible = bool(search_state["open"])

        if not search_state["open"] and search_state["query"]:
            search_field.value = ""
            search_state["query"] = ""
            tiles_col.controls = build_tiles()

        page.update()

    def on_search(e):
        search_state["query"] = search_field.value or ""
        tiles_col.controls = build_tiles()
        page.update()

    search_field = ft.TextField(
        hint_text="search e.g. tutoring",
        prefix_icon=ft.Icons.SEARCH,
        filled=True,
        border=ft.InputBorder.NONE,
        border_radius=12,
        content_padding=10,
        text_size=14,
        on_change=on_search,
    )

    search_box = ft.Container(
        visible=False,
        padding=ft.Padding.symmetric(horizontal=16, vertical=4),
        content=search_field,
    )

    tiles_col = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        expand=True,
        controls=build_tiles(),
    )

    return ft.View(
        route="/GetPaid",
        padding=0,
        controls=[
            ft.Container(
                padding=ft.Padding.only(left=16, right=16, top=24, bottom=8),
                content=ft.Column(
                    spacing=2,
                    controls=[
                        ft.Text(
                            "What would you like to offer?",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            "Choose how you'd like to help.",
                            size=13,
                            color=ft.Colors.GREY_600,
                        ),
                    ],
                ),
            ),
            search_box,   # <<< MOVE THIS LINE TO CHANGE THE SEARCH BAR POSITION
            tiles_col,
        ],
    )