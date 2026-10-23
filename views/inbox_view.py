import flet as ft


def inbox(page: ft.Page, request_preview, fhchat):

    def go_home():
        page.navigate("/home")

    # Reopens the chat that was tapped
    def open_chat(e):
        kind, info = e.control.data
        if kind == "feed":
            request_preview.selected = info
            page.navigate("/chat")
        else:
            fhchat.selected = info
            page.navigate("/fhchat")

    # One neat row per chat: name + your last message
    def make_row(name, last_message, kind, info):
        return ft.ListTile(
            data=(kind, info),
            on_click=open_chat,
            leading=ft.CircleAvatar(
                radius=20,
                bgcolor=ft.Colors.ORANGE,
                content=ft.Text(
                    name[0].upper(),
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
            ),
            title=ft.Text(name, weight=ft.FontWeight.W_600),
            subtitle=ft.Text(
                f"You: {last_message}",
                max_lines=1,
                overflow=ft.TextOverflow.ELLIPSIS,
                size=13,
                color=ft.Colors.GREY_600,
            ),
            trailing=ft.Icon(icon=ft.Icons.CHEVRON_RIGHT, color=ft.Colors.GREY_500),
        )

    # ---------- Collect the chats that have messages ----------
    rows = []

    # Chats started from the feed ("I can help")
    for key, msgs in getattr(request_preview, "messages", {}).items():
        if msgs:
            info = request_preview.chat_info[key]
            rows.append(make_row(info[0]["name"], msgs[-1], "feed", info))

    # Chats started from Find Help
    for key, msgs in getattr(fhchat, "messages", {}).items():
        if msgs:
            info = fhchat.chat_info[key]
            rows.append(make_row(info["name"], msgs[-1], "fh", info))

    # Shown when there are no chats yet
    tip = ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
                ft.Icon(icon=ft.Icons.CHAT_BUBBLE_OUTLINE, size=30, color=ft.Colors.GREY_500),
                ft.Text("No messages yet", size=16, weight=ft.FontWeight.W_500, color=ft.Colors.GREY_800),
                ft.Text("Tap 'I can help' on a post to start one", size=12, color=ft.Colors.GREY_600),
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.Alignment(0, 0),
    )

    return ft.View(
        route="/inbox",
        controls=[
            ft.AppBar(
                title=ft.Text("Chats", size=18, weight=ft.FontWeight.BOLD),
                center_title=True,
                leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, tooltip="go back", on_click=go_home),
            ),
            ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                controls=rows if rows else [tip],
            ),
        ],
    )