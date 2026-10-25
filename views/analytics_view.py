import flet as ft
import asyncio
from business_logic.posts import Feed
from datetime import datetime


def analytics(page: ft.Page, feed: Feed):

    LEVELS = ["Start at R0", "Small budget", "Bigger budget"]

    IDEAS = {
        "Event & party hire": {
            LEVELS[0]: {
                "title": "Party Helper (R0 start)",
                "steps": [
                    "Ask neighbours and people at church: who owns chairs or coolers near Zone 3?",
                    "Make a list of 5 people who hire them out",
                    "Post: \"Chairs + coolers for hire near Zone 3, message me\"",
                ],
                "charge": "Estimate: 1 party found = R100 finder fee\n5 parties = R500 per weekend",
                "note": "Only take the finder fee, never the hire money. Don't promise chairs you haven't seen.",
                },
            LEVELS[1]: {
                "title": "1 Cooler Hustle",
                "steps": [
                    "Buy 1 big cooler (R500), ice bags (R100), cleaning stuff (R100) and data for posts (R100) = R800",
                    "Ask your Level 0 contacts and church: who has a party this weekend?",
                    "Rent your cooler out for R150 per party",
                ],
                "charge": "Estimate: 1 party x R150 = R150\n4 parties a month = R600 per month",
                "note": "Always take a R100 deposit. No deposit, no cooler. If it breaks, you lose.",
            },
            LEVELS[2]: {
                "title": "Event Boss",
                "steps": [
                    "Buy 20 chairs (R3,000), 2 coolers (R1,000), 1 table (R1,000) and transport (R3,000) = R8,000",
                    "Hand out flyers at church and schools, and ask your Level 1 customers to refer you",
                    "Rent out the full pack for parties in Zone 3",
                ],
                "charge": "Estimate: 1 party = R900 hire\n4 parties a month = R3,600 per month\nPaid off in about 2-3 months",
                "note": "Keep hire money separate from your own. If you spend the R900, you can't fix broken chairs.",
            },
        },
        "Family care & check-ins": {
            LEVELS[0]: {
                "title": "Check-in Helper (R0 start)",
                "steps": [
                    "Ask neighbours and people at church: who stays alone in the community?",
                    "Make a list of 5 elderly people who would like regular visits",
                    "Visit them: cook small meals, help them walk, and keep them company",
                ],
                "charge": "Estimate: 1 check-in = R80\n3 check-ins a day = R240 per day",
                "note": "This is not nursing. Never give injections or medicine, only help and check in.",
            },
        
            LEVELS[1]: {
                "title": "Caregiver Hustle",
                "steps": [
                    "Buy a uniform (R300), gloves (R100) and a small bag (R100) = R500",
                    "Find families at the clinic and church, and ask your first clients to tell other families",
                    "Stay 3 hours with one person instead of a 30-minute check-in",
                ],
                "charge": "Estimate: 1 family x R150 per day x 5 days = R750 per week",
                "note": "Never take money from the elderly person's grant. Only take payment from the family.",
            },
            LEVELS[2]: {
                "title": "Care Boss",
                "steps": [
                    "Buy 3 uniforms (R900), a first aid kit (R500) and flyers (R500) = about R2,000",
                    "Hand out flyers at the clinic and church, and ask your Level 1 families to refer you",
                    "Find 3 helpers in your area: you find the families, they do the visits",
                    "Keep the rest of your budget as a buffer to pay helpers before families pay you",
                ],
                "charge": "Estimate: 3 families x R750 = R2,250 per week\n3 helpers x R500 = R1,500\nYou keep about R750 per week",
                "note": "Keep your helpers' pay separate from your own money. If you spend their pay, they quit and you lose families.",
            },
        },
        "Rooms & places to rent": {
            LEVELS[0]: {
                "title": "Room Finder (R0 start)",
            "steps": [
                "Ask neighbours and people at church: who has an empty backroom?",
                "Make a list of 5 landlords",
                "Post: \"Rooms to rent in [your area], message me\" on socials",
            ],
            "charge": "Estimate: 1 room found = R200 finder fee\n5 rooms = R1,000 per month",
            "note": "Only take the finder fee, never the rent. Don't promise a room you haven't seen.",
            },
            LEVELS[1]: {
                "title": "Room Manager",
                "steps": [
                    "Ask your landlord contacts for one dirty empty room you can fix up",
                    "Buy cleaning stuff (R200), a curtain (R200) and data for photos and calls (R100) = R500",
                    "Clean it, hang the curtain, post nice photos and find the tenant for the owner",
                ],
                "charge": "Estimate: 1 room rented = R500 once-off\n+ R200 every month you manage it",
                "note": "The room is not yours. Only clean it and find a tenant for the owner.",
            },
            
            LEVELS[2]: {
                "title": "Yard Boss",
                "steps": [
                    "Build 2 backrooms in your own yard for about R15,000",
                    "Check that your municipality allows backrooms before you build",
                    "Find tenants through church and posts like \"Rooms in my yard, [your area]\"",
                    "Add a mattress and curtain to each room",
                ],
                "charge": "Estimate: 2 rooms x R1,000 = R2,000 per month\nPaid off in about 8 months",
                "note": "Keep rent money separate from your own. You will need it to fix leaks and electricity.",
            },
        },
    }

    def get_idea(name, level):
        if name in IDEAS:
            return IDEAS[name][level]
        generic = {
            LEVELS[0]: {
                "title": f"Start a '{name}' service (R0 start)",
                "steps": [
                    "Ask 3 neighbours who posted this need what they would pay",
                    "Start with one customer and ask for a review",
                    "List it in Offer Help so others can find you",
                ],
                "charge": "Estimate: depends on the service. Set your price after your first jobs.",
                "note": "This is a general starting idea.",
            },
            LEVELS[1]: {
                "title": f"Grow your '{name}' service",
                "steps": [
                    "Use your first earnings to buy basic supplies or tools",
                    "Share a simple flyer with your price and contact",
                    "Ask every customer for a review so new people trust you",
                ],
                "charge": "Estimate: depends on the service and how many customers you get.",
                "note": "This is a general starting idea.",
            },
            LEVELS[2]: {
                "title": f"Build a '{name}' business",
                "steps": [
                    "Register the business and set up proper equipment",
                    "Hire or train a helper so you can take more jobs",
                    "Offer regular packages to households and local shops",
                ],
                "charge": "Estimate: depends on the service and the size of your team.",
                "note": "This is a general starting idea.",
            },
        }
        return generic[level]

    async def type_text(control, full_text, animate=True):
        if not animate:
            control.value = full_text
            control.update()
            return
        control.value = ""
        for i in range(2, len(full_text) + 2, 2):
            control.value = full_text[:i]
            control.update()
            await asyncio.sleep(0.02)

    def make_step(num):
        text = ft.Text("", size=15)
        row = ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=12,
            controls=[
                ft.CircleAvatar(
                    content=ft.Text(str(num), size=12),
                    radius=12,
                    bgcolor=ft.Colors.BLUE_700,
                ),
                ft.Container(text, expand=True),
            ],
        )
        return row, text

    async def open_idea(name):
        state = {"level": LEVELS[0], "busy": True}

        thinking = ft.Row(
            spacing=10,
            controls=[
                ft.ProgressRing(width=16, height=16, stroke_width=2),
                ft.Text("Preparing idea...", size=14, italic=True),
            ],
        )
        content = ft.Column(tight=True, spacing=18)
        chips_row = ft.Row(spacing=8, wrap=True)

        def chip(level):
            selected = state["level"] == level
            return ft.Container(
                content=ft.Text(level, size=13),
                padding=ft.Padding(left=12, right=12, top=6, bottom=6),
                border_radius=16,
                bgcolor=ft.Colors.with_opacity(0.4 if selected else 0.1, ft.Colors.ORANGE),
                on_click=lambda e, l=level: pick(l),
            )

        async def render(level, animate):
            idea = get_idea(name, level)
            state["busy"] = True
            content.controls.clear()
            content.update()

            title = ft.Text("", size=20, weight=ft.FontWeight.BOLD)
            content.controls.append(title)
            content.update()
            await type_text(title, idea["title"], animate)

            content.controls.append(ft.Text("What you'd do", weight=ft.FontWeight.W_600))
            for i, s in enumerate(idea["steps"], start=1):
                row, text = make_step(i)
                content.controls.append(row)
                content.update()
                await type_text(text, s, animate)

            if animate:
                await asyncio.sleep(0.4)
            content.controls.append(
                ft.Container(
                    padding=14,
                    border_radius=12,
                    bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.GREEN),
                    content=ft.Text(idea["charge"], size=15),
                )
            )
            content.controls.append(
                ft.Row([
                    ft.Icon(ft.Icons.INFO_OUTLINE, size=18),
                    ft.Container(ft.Text(idea["note"], size=13), expand=True),
                ])
            )
            content.update()
            state["busy"] = False

        async def safe_render(level, animate):
            try:
                await render(level, animate)
            except RuntimeError:
                return

        def pick(level):
            if state["busy"] or level == state["level"]:
                return
            state["level"] = level
            chips_row.controls = [chip(l) for l in LEVELS]
            chips_row.update()
            page.run_task(safe_render, level, False)
            

        chips_row.controls = [chip(l) for l in LEVELS]

        page.show_dialog(
            ft.BottomSheet(
                ft.Container(
                    padding=24,
                    content=ft.Column(
                        tight=True,
                        spacing=18,
                        scroll=ft.ScrollMode.AUTO,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.AUTO_AWESOME, color=ft.Colors.AMBER),
                                ft.Text("Suggested idea", size=13),
                            ]),
                            chips_row,
                            thinking,
                            content,
                        ],
                    ),
                )
            )
        )

        try:
            await asyncio.sleep(1.5)
            thinking.visible = False
            thinking.update()
            await render(state["level"], True)
        except RuntimeError:
            return

    # ---------- The chart: calculated fresh every time this screen opens ----------
    needs = feed.get_needs()
    trends = feed.get_trends()

    TAG_STYLE = {
        "growing": ("↑ growing", ft.Colors.GREEN),
        "steady": ("→ steady", ft.Colors.GREY),
        "slowing": ("↓ slowing", ft.Colors.RED_300),
    }

    def tag_chip(tag):
        label, color = TAG_STYLE[tag]
        return ft.Container(
            content=ft.Text(label, size=11, color=color),
            padding=ft.Padding(left=8, right=8, top=2, bottom=2),
            border_radius=10,
            bgcolor=ft.Colors.with_opacity(0.15, color),
        )
    max_total = max([n["total"] for n in needs]) if needs else 1
    #max_bar_width = 280

    def make_row(item):
        name = item["need"]
        total = item["total"]
        open_count = item["open"]
        helped_count = total - open_count

        segments = []
        if open_count:
            segments.append(ft.Container(expand=open_count, height=28, bgcolor=ft.Colors.ORANGE))
        if helped_count:
            segments.append(ft.Container(expand=helped_count, height=28, bgcolor=ft.Colors.with_opacity(0.35, ft.Colors.ORANGE)))

        bar_parts = [
            ft.Container(
                expand=total,
                height=28,
                border_radius=8,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=ft.Row(spacing=0, controls=segments),
            )
        ]
        if max_total - total:
            bar_parts.append(ft.Container(expand=max_total - total, height=28))

        return ft.Container(
            on_click=lambda e, n=name: page.run_task(open_idea, n),
            content=ft.Column(
                spacing=6,
                controls=[
                    ft.Text(name, size=16),
                    ft.Row(spacing=0, controls=bar_parts),
                    ft.Text(f"{total} requests · {open_count} still open", size=13, color=ft.Colors.GREY_500),
                ],
            ),
        )

    if needs:
        chart = ft.Column(
            spacing=24,
            horizontal_alignment= ft.CrossAxisAlignment.STRETCH,
            controls=[make_row(item) for item in needs],
        )
    else:
        chart = ft.Text("Not enough requests yet to show a pattern.", italic=True)


    def make_trend_row(item):
        name = item["need"]
        t = trends[name]
        top = max(t["two_weeks_ago"], t["last_week"], t["this_week"], t["next_week"], 1)
        max_h = 60

        def column(label, value, estimate=False):
            color = ft.Colors.with_opacity(0.35, ft.Colors.TEAL) if estimate else ft.Colors.TEAL
            return ft.Column(
                spacing=4,
                expand= True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(str(value), size=13, weight=ft.FontWeight.BOLD),
                    ft.Container(width=40, height=max(4, max_h * value / top), bgcolor=color, border_radius=6),
                    ft.Text(label, size=11, color=ft.Colors.GREY_500),
                ],
            )

        return ft.Column(
            spacing=10,
            controls=[
                ft.Row([ft.Text(name, size=15), tag_chip(t["tag"])], spacing=8),
                ft.Row(
                    spacing=0,
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    controls=[
                        column("2 wks ago", t["two_weeks_ago"]),
                        column("last week", t["last_week"]),
                        column("this week", t["this_week"]),
                        column("next (est.)", t["next_week"], estimate=True),
                    ],
                ),
            ],
        ) 

    trend_card = ft.Container(
        visible=bool(needs),
        padding=20,
        border_radius=16,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
        content=ft.Column(
            spacing=22,
            controls=[
                #ft.Text("Trend and forecast", size=16),
                ft.Text("All requests over the last 3 weeks, plus a simple estimate for next week.", size=13, color=ft.Colors.GREY_500),
                *[make_trend_row(item) for item in needs],
                ft.Text("Estimate based on sample data, not a real prediction.", size=12, italic=True, color=ft.Colors.GREY_500),
            ],
        ),
    )

    #posts_length = len(feed.posts) + len(feed.new_posts)
    posts_length = len([p for p in feed.posts + feed.new_posts if (datetime.now() - p["time_stamp"]).days < 7])

    return ft.View(
        route="/analytics",
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.AppBar(
                title=ft.Text("Turn gaps into income"),
                center_title=True,
            ),
            ft.ResponsiveRow(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        col={"xs": 12, "md": 8, "lg": 6},
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                        spacing=12,
                        controls=[
                            ft.Text("Most requested needs this week", size=16),
                            ft.Container(
                                padding=20,
                                border_radius=16,
                                bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                                content=chart,
                            ),
                            ft.Text("\U00002728 Tap a bar to see how you could turn it into a service", size=14, color="grey", italic=True),

                            ft.Container(height=10),
                            ft.Text("Trend and Forecast", size= 16),
                            trend_card,
                            ft.Text(f"Based on {posts_length} requests this week (sample data)", italic=True, size=14),
                        ],
                    ),
                ],
            ),
        ],
    )