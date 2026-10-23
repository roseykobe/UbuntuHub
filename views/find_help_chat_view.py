import flet as ft
from business_logic.fhchat import findh_chat
from views.profile_view import profile


def fh_chat(page: ft.Page, fhchat: findh_chat):
    

    data = fhchat.selected

    # Messages are kept on fhchat, so they survive screen changes
    if not hasattr(fhchat, "messages"):
        fhchat.messages = {}

    chat_key = (data["helper_id"], data["offer"])
    saved = fhchat.messages.setdefault(chat_key, [])

    if not hasattr(fhchat, "chat_info"):
        fhchat.chat_info = {}
    fhchat.chat_info[chat_key] = data

    def open_profile(e):
            fhchat.profile_id= data["helper_id"]
            page.navigate("/profile")
        
    

    # ---------- helpers ----------

    def make_message(content: str):
        # A Row with alignment END pushes the bubble to the right side
        return ft.Row(
            alignment=ft.MainAxisAlignment.END,
            controls=[
                ft.Container(
                    padding=12,
                    margin=ft.Margin.symmetric(horizontal=12, vertical=4),
                    bgcolor=ft.Colors.ORANGE_100,
                    border_radius=8,
                    content=ft.Text(
                        content,
                        size=13,
                        color=ft.Colors.ORANGE_800,
                    ),
                )
            ],
        )

    # ---------- events ----------

    def check_field(e):
        send_btn.disabled = not text.value.strip()
        page.update()

    def send_message(e):
        content = text.value.strip()

        if not content:
            return

        saved.append(content)
        # Add the new bubble to the end of the column
        # (do NOT clear the column, that removes the "replying to" card)
        scroll_column.controls.append(make_message(content))

        # Reset the input and disable the button again
        text.value = ""
        send_btn.disabled = True

        page.update()

    def back(e):
        page.navigate("/FindHelp")

    # ---------- controls ----------

    text = ft.TextField(
        hint_text="Reply...",
        filled=True,
        border=ft.InputBorder.NONE,
        content_padding=0,
        text_size=14,
        height=40,
        expand=True,
        multiline=True,
        on_change=check_field,
    )

    send_btn = ft.IconButton(
        icon=ft.Icons.SEND_ROUNDED,
        icon_color=ft.Colors.BLUE,
        icon_size=18,
        bgcolor=ft.Colors.ORANGE_50,
        disabled=True,
        on_click=send_message,
    )

    scroll_column = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        auto_scroll=True,  # jumps to the newest message automatically
        controls=[
            ft.Container(
                padding=12,
                margin=ft.Margin.symmetric(horizontal=12, vertical=8),
                bgcolor=ft.Colors.ORANGE_50,
                border_radius=8,
                content=ft.Column(
                    spacing=6,
                    controls=[
                        ft.Text(
                            "You're replying to:",
                            size=12,
                            color=ft.Colors.GREY_600,
                        ),
                        ft.Text(
                            f"{data['offer']}",
                            size=14,
                            weight=ft.FontWeight.W_500,
                            color=ft.Colors.ORANGE_800,
                        ),
                        ft.Row(
                            spacing=4,
                            alignment=ft.MainAxisAlignment.START,
                            controls=[
                                ft.Text(
                                    f"Offered by: {data['name']}",
                                    size=13,
                                    color=ft.Colors.BLUE_GREY_700,
                                )
                                #ft.Icon(
                                    #ft.Icons.VERIFIED,
                                    #size=16,
                                    #color=ft.Colors.BLUE_200,
                                #),
                            ],
                        ),
                        #ft.FilledButton(
                            #"Done",
                            #bgcolor=ft.Colors.ORANGE_800,
                            #disabled=True,
                        #),
                    ],
                ),
            ),
        ],
    )
    for old in saved:
        scroll_column.controls.append(make_message(old))

    input_bar = ft.Container(
        padding=10,
        margin=ft.Margin.symmetric(horizontal=12, vertical=8),
        bgcolor=ft.Colors.WHITE,
        border_radius=30,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        content=ft.Row(
            spacing=8,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[text, send_btn],
        ),
    )

    #title_items= [ft.Text(data["header"])]
    #if data["verified"]
    appbar = ft.AppBar(
        leading=ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            tooltip="go back",
            on_click=back,
        ),
        title= ft.GestureDetector(on_tap= open_profile, content=ft.Row(controls= data['header'], alignment= ft.MainAxisAlignment.CENTER,))
        #center_title= True
    )

    return ft.View(
        route="/fhchat",
        appbar=appbar,
        controls=[
            scroll_column,
            input_bar,
        ],
    )