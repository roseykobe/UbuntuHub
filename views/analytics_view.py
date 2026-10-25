import flet as ft
import asyncio
from business_logic.posts import Feed


def analytics(page: ft.Page, feed: Feed):

    IDEAS = {
        "Family care & check-ins": {
            "title": "Start a 'Care help' service",
            "steps": [
                "Visit 3x a week for 30 minutes",
                "Sweep, make tea, check they ate and took meds",
                "Send the family a voice note: 'Gogo is fine today'",
            ],
            "charge": "Estimate: R600-900 per month per gogo\n3 gogos = R1800-R2700/month",
            "note": "This is NOT nursing. No injections. You are help.",
        },
        "Event & party hire": {
            "title": "Event Hire Middleman (R0 start)",
            "steps": [
                "Find neighbours with chairs or coolers they aren't using. Take photos and agree on a price",
                "List them at R10 per chair or R150 per cooler per day, plus delivery",
                "When someone orders, rent from the owner (R6 per chair, R80 per cooler) and keep the difference",
            ],
            "charge": "Estimate: 20 chairs x R4 = R80 per event\n4 coolers x R70 = R280 per weekend\n+ delivery fees",
            "note": "You don't need to own any stock to start.",
        },
        "Neighbourhood safety": {
            "title": "Safe-walk buddy (R0 start)",
            "steps": [
                "Agree with 2 or 3 parents to walk their children home from the bus stop",
                "Walk as a group at a fixed time, and message each parent when their child is home",
                "Ask the parents for a short review after the first month",
            ],
            "charge": "Estimate: R100-150 per child per month\n5 children = R500-750/month",
            "note": "Always get the parent's permission first, and walk in a group, never alone with one child.",
        },
    }

    def get_idea(name):
        if name in IDEAS:
            return IDEAS[name]
        return {
            "title": f"Start a '{name}' service",
            "steps": [
                "Ask 3 neighbours who posted this need what they would pay",
                "Start with one customer and ask for a review",
                "List it in Offer Help so others can find you",
            ],
            "charge": "Estimate: depends on the service. Start small and set your price after your first jobs.",
            "note": "This is a general starting idea.",
        }

    async def type_text(control, full_text):
        # Types the text out 2 characters at a time
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
        idea = get_idea(name)

        # 1. Sheet opens with a short loading state
        thinking = ft.Row(
            spacing=10,
            controls=[
                ft.ProgressRing(width=16, height=16, stroke_width=2),
                ft.Text("Preparing idea...", size=14, italic=True),
            ],
        )
        content = ft.Column(tight=True, spacing=18)

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
                            thinking,
                            content,
                        ],
                    ),
                )
            )
        )

        # 2. Short pause, then hide the loading state
        await asyncio.sleep(1.5)
        thinking.visible = False
        thinking.update()

        # 3. Type out the title
        title = ft.Text("", size=20, weight=ft.FontWeight.BOLD)
        content.controls.append(title)
        content.update()
        await type_text(title, idea["title"])

        # 4. Type out each step, one after the other
        content.controls.append(ft.Text("What you'd do", weight=ft.FontWeight.W_600))
        for i, s in enumerate(idea["steps"], start=1):
            row, text = make_step(i)
            content.controls.append(row)
            content.update()
            await type_text(text, s)

        # 5. Money box and note appear at the end
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
    max_bar_width = 280

    def make_row(item):
        trend = trends.get(item["need"])
        name = item["need"]
        total = item["total"]
        open_count = item["open"]
        helped_count = total - open_count

        return ft.Container(
            on_click=lambda e, n=name: page.run_task(open_idea, n),
            content=ft.Column(
                spacing=6,
                controls=[
                    #ft.Text(name, size=16),
                    ft.Row([ft.Text(name, size=16)] + ([tag_chip(trend["tag"])] if trend else []), spacing=8),
                    ft.Container(
                        width=max_bar_width * total / max_total,
                        height=28,
                        border_radius=8,
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        content=ft.Row(
                            spacing=0,
                            controls=[
                                ft.Container(
                                    width=max_bar_width * open_count / max_total,
                                    height=28,
                                    bgcolor=ft.Colors.ORANGE,
                                ),
                                ft.Container(
                                    width=max_bar_width * helped_count / max_total,
                                    height=28,
                                    bgcolor=ft.Colors.with_opacity(0.35, ft.Colors.ORANGE),
                                ),
                            ],
                        ),
                    ),
                    ft.Text(f"{total} requests · {open_count} still open", size=13, color=ft.Colors.GREY_500),
                ],
            ),
        )

    if needs:
        chart = ft.Column(
            spacing=24,
            controls=[make_row(item) for item in needs],
        )
    else:
        chart = ft.Text("Not enough requests yet to show a pattern.", italic=True)

    def make_trend_row(item):
        name = item["need"]
        t = trends[name]
        top = max(t["earlier"], t["recent"], t["next"], 1)
        max_h = 60

        def column(label, value, estimate=False):
            color = ft.Colors.with_opacity(0.35, ft.Colors.ORANGE) if estimate else ft.Colors.ORANGE
            return ft.Column(
                spacing=4,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(str(value), size=13, weight=ft.FontWeight.BOLD),
                    ft.Container(width=44, height=max(4, max_h * value / top), bgcolor=color, border_radius=6),
                    ft.Text(label, size=11, color=ft.Colors.GREY_500),
                ],
            )

        return ft.Column(
            spacing=10,
            controls=[
                ft.Row([ft.Text(name, size=15), tag_chip(t["tag"])], spacing=8),
                ft.Row(
                    spacing=28,
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    controls=[
                        column("before", t["earlier"]),
                        column("last 3 days", t["recent"]),
                        column("next 3 (est.)", t["next"], estimate=True),
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
                ft.Text("Trend and forecast", size=16),
                ft.Text("Requests in the 3 days before, the last 3 days, and a simple estimate for the next 3.", size=13, color=ft.Colors.GREY_500),
                *[make_trend_row(item) for item in needs],
                ft.Text("Estimate based on sample data, not a real prediction.", size=12, italic=True, color=ft.Colors.GREY_500),
            ],
        ),
    )

    posts_length = len(feed.posts) + len(feed.new_posts)

    return ft.View(
        route="/analytics",
        horizontal_alignment= ft.CrossAxisAlignment.STRETCH,
        controls=[
            ft.AppBar(
                title=ft.Text("Turn gaps into income"),
                center_title=True,
            ),
            ft.Column( 
                scroll= ft.ScrollMode.AUTO,
                expand= True,
                controls= [
            ft.Text("Most requested needs this week", size=16),
            #ft.Text("Bright part: still open. Light part: already helped.", size=13, color=ft.Colors.GREY_500),
            ft.Container(
                padding=20,
                border_radius=16,
                bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                content=chart,
            
            ),
            
            ft.Text("\U00002728 Tap a bar to see how you could turn it into a service", size=14, color="grey", italic=True),
            ft.Text(f"Based on {posts_length} requests (sample data)", italic=True, size=14),
            ft.Container(height=20),

            ft.Text("Trends and Forecast"),
            trend_card,
                ]
                
            )
        ],
    )