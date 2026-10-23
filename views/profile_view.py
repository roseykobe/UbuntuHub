import flet as ft

# Show the average rating only after this many ratings
MIN_RATINGS = 3


def profile(page: ft.Page, offers, helper_id):
    user = offers.users[helper_id]
    name = user["name"]

    def back(e):
        page.navigate("/fhchat")

    # Small message at the bottom of the screen
    def toast(text):
        page.show_dialog(
            ft.SnackBar(
                ft.Text(text),
                duration=2000,
                behavior=ft.SnackBarBehavior.FLOATING,
                margin=ft.Margin.only(bottom=100, left=20, right=20),
            )
        )
        page.update()

    # ---------- Ratings ----------
    # Draws 5 stars (full, half or empty) for an average
    def star_row(avg, size=22):
        rounded = round(avg * 2) / 2
        stars = []
        for i in range(1, 6):
            if rounded >= i:
                icon = ft.Icons.STAR
            elif rounded >= i - 0.5:
                icon = ft.Icons.STAR_HALF
            else:
                icon = ft.Icons.STAR_BORDER
            stars.append(ft.Icon(icon=icon, color=ft.Colors.AMBER, size=size))
        return ft.Row(controls=stars, spacing=0, alignment=ft.MainAxisAlignment.CENTER)

    rating_box = ft.Container()

    reviews_box = ft.Column(spacing=8)

    def build_reviews():
        reviews_box.controls.clear()
        reviews_box.controls.append(
            ft.Text("Reviews", size=14, weight=ft.FontWeight.BOLD)
        )

        #reviews = offers.get_reviews(helper_id)
        reviews= []
        for r in offers.get_reviews(helper_id):
            if r["comment"].strip():
                reviews.append(r)

        if not reviews:
            reviews_box.controls.append(
                ft.Text("No reviews yet.", color=ft.Colors.GREY_600)
            )
            return

        for r in reviews:
            reviewer = offers.users.get(r["reviewer_id"], {})
            reviewer_name = reviewer.get("name", "Someone")

            lines = [
                ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(reviewer_name, weight=ft.FontWeight.W_600),
                    star_row(r["stars"], size=14),
                ],
            )
        ]
            if r["comment"]:
                lines.append(ft.Text(r["comment"], size=13))

            reviews_box.controls.append(
                ft.Container(
                bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.ON_SURFACE),
                border_radius=12,
                padding=12,
                content=ft.Column(spacing=4, controls=lines),
            )
        )

    # Rebuilds the rating area (also called after a new review)
    def build_rating():
        avg, count = offers.get_rating(helper_id)

        if count == 0:
            rating_box.content = ft.Text(
                "New helper · no ratings yet", color=ft.Colors.GREY_600
            )
        elif count < MIN_RATINGS:
            word = "rating" if count == 1 else "ratings"
            rating_box.content = ft.Text(
                f"New helper · {count} {word}", color=ft.Colors.GREY_600
            )
        else:
            rating_box.content = ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=2,
                controls=[
                    ft.Text(f"{avg:.1f}", size=32, weight=ft.FontWeight.BOLD),
                    star_row(avg),
                    ft.Text(f"{count} ratings", size=12, color=ft.Colors.GREY_600),
                ],
            )

    # ---------- Add review popup ----------
    def open_review(e):
        if offers.has_reviewed(helper_id):
            toast(f"You've already reviewed {name}.")
            return
        chosen = {"stars": 0}
        star_icons = []
        star_boxes = []

        comment = ft.TextField(
            hint_text=f"Say something about {name} (optional)",
            multiline=True,
            min_lines=2,
            max_lines=4,
            max_length=150,
        )
        error = ft.Text("", color=ft.Colors.RED, size=12)

        def pick(ev):
            chosen["stars"] = ev.control.data
            number = 1
            for icon in star_icons:
                if number <= chosen["stars"]:
                    icon.icon = ft.Icons.STAR
                else:
                    icon.icon = ft.Icons.STAR_BORDER
                number += 1
            page.update()

        for i in range(1, 6):
            icon = ft.Icon(icon=ft.Icons.STAR_BORDER, color=ft.Colors.AMBER, size=34)
            star_icons.append(icon)
            star_boxes.append(ft.GestureDetector(data=i, on_tap=pick, content=icon))

        def cancel(ev):
            page.pop_dialog()

        def submit(ev):
            if chosen["stars"] == 0:
                error.value = "Please tap a star rating."
                page.update()
                return
            offers.add_review(helper_id, chosen["stars"], comment.value or "")
            page.pop_dialog()
            build_rating()
            build_reviews()
            page.update()
            toast("Thanks for your review!")

        page.show_dialog(
            ft.AlertDialog(
                modal=True,
                title=ft.Text(f"Review {name}"),
                content=ft.Column(
                    tight=True,
                    width=280,
                    controls=[
                        ft.Row(
                            controls=star_boxes,
                            spacing=6,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        error,
                        comment,
                    ],
                ),
                actions=[
                    ft.TextButton("Cancel", on_click=cancel),
                    ft.TextButton("Submit", on_click=submit),
                ],
            )
        )

    # ---------- Report popup ----------
    def open_report(e):
        reason = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Radio(value="Fake or misleading", label="Fake or misleading"),
                    ft.Radio(value="Rude or abusive", label="Rude or abusive"),
                    ft.Radio(value="Unsafe behaviour", label="Unsafe behaviour"),
                    ft.Radio(value="Other", label="Other"),
                ]
            )
        )
        error = ft.Text("", color=ft.Colors.RED, size=12)

        def cancel(ev):
            page.pop_dialog()

        def submit(ev):
            if not reason.value:
                error.value = "Please choose a reason."
                page.update()
                return
            offers.add_report(helper_id, reason.value)
            page.pop_dialog()
            toast("Report sent. Thank you.")

        page.show_dialog(
            ft.AlertDialog(
                modal=True,
                title=ft.Text(f"Report {name}"),
                content=ft.Column(
                    tight=True,
                    width=280,
                    controls=[reason, error],
                ),
                actions=[
                    ft.TextButton("Cancel", on_click=cancel),
                    ft.TextButton(
                        "Send report",
                        on_click=submit,
                        style=ft.ButtonStyle(color=ft.Colors.RED),
                    ),
                ],
            )
        )

    # ---------- Picture, name + verified badge ----------
    # Shows the photo if the user has a "photo", otherwise the first letter
    avatar = ft.CircleAvatar(
        radius=50,
        bgcolor=ft.Colors.ORANGE,
        foreground_image_src=user.get("photo"),
        content=ft.Text(
            name[0].upper(),
            size=36,
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.BOLD,
        ),
    )

    name_row = [ft.Text(name, size=22, weight=ft.FontWeight.BOLD)]
    if user.get("verified"):
        name_row.append(
            ft.Icon(icon=ft.Icons.VERIFIED, color=ft.Colors.BLUE, size=20)
        )

    # ---------- Bio ----------
    bio_card = ft.Container(
        bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.ON_SURFACE),
        border_radius=12,
        padding=15,
        margin=ft.Margin.only(left=16, right=16),
        content=ft.Column(
            spacing=4,
            controls=[
                ft.Text("About", size=14, weight=ft.FontWeight.BOLD),
                ft.Text(user.get("bio", "No bio yet.")),
            ],
        ),
    )

    # First draw of the rating area
    build_rating()
    build_reviews()

    return ft.View(
        route="/Profile",
        controls=[
            ft.AppBar(
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    tooltip="go back",
                    on_click=back,
                ),
                title=ft.Text("Profile"),
            ),
            ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=14,
                controls=[
                    ft.Container(height=10),
                    avatar,
                    ft.Row(
                        controls=name_row,
                        spacing=6,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    rating_box,
                    bio_card,
                    ft.Row(
                        spacing=15,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.FilledButton(
                                "Add review",
                                icon=ft.Icons.RATE_REVIEW,
                                bgcolor=ft.Colors.ORANGE,
                                color=ft.Colors.WHITE,
                                on_click=open_review,
                            ),
                            ft.OutlinedButton(
                                "Report",
                                icon=ft.Icons.FLAG_OUTLINED,
                                style=ft.ButtonStyle(color=ft.Colors.RED),
                                on_click=open_report,
                            ),
                        ],
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(
                                expand=True,
                                margin=ft.Margin.only(left=16, right=16),
                                content=reviews_box,
                            )
                        ]
                    ),
                ],
            ),
        ],
    )