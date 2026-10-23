import flet as ft
#from business_logic.feed import chat_preview
from business_logic.posts import chat_preview
from business_logic.posts import Feed



def chat(page: ft.Page, request_preview: chat_preview):

    post= request_preview.selected
    

    def open_profile(e):
    
        data= post[0]
        request_preview.profile_id= data["id"]
        
        page.navigate("/profile1") 
         
    
    
    user= post[0]
    postt= post[1]
    if not hasattr(request_preview, "messages"):
        request_preview.messages= {}

    chat_key= (user["id"], postt["id"])
    saved= request_preview.messages.setdefault(chat_key, [])

    if not hasattr(request_preview, "chat_info"):
        request_preview.chat_info = {}
    request_preview.chat_info[chat_key] = post

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

    def check_field(e):
            send_btn.disabled = not text.value.strip()
            page.update()
    
    def send_message(e):
        content = text.value.strip()
    
        if not content:
            return
        
        saved.append(content)
        scroll_column.controls.append(make_message(content))
        text.value = ""
        send_btn.disabled = True
        
        page.update()
        
    def to_feed():
        page.navigate("/home")

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
                                "You're offering to help with:",
                                size=12,
                                color=ft.Colors.GREY_600,
                            ),
                            ft.Text(
                                f"{postt['text']}",
                                size=14,
                                weight=ft.FontWeight.W_500,
                                color=ft.Colors.ORANGE_800,
                            ),
                            ft.Row(
                                spacing=4,
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Text(
                                        f"Offered by: {user['name']}",
                                        size=13,
                                        color=ft.Colors.BLUE_GREY_700,
                                    ),
                                    #ft.Icon(
                                        #ft.Icons.VERIFIED,
                                        #size=16,
                                        #color=ft.Colors.BLUE_200,
                                    #),
                                ],
                            ),
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
    

    
    def post_preview(post):
        poster=ft.Container(
            padding= 12, 
            margin= 10,
            bgcolor=ft.Colors.ON_SURFACE_VARIANT,
            border_radius=8,
            content= ft.Column(
                controls= [
                    ft.Text(f"You're offering to help with:", size= 12, color= ft.Colors.GREY_600),
                    ft.Text(f"{post['request']}", size= 14, weight= ft.FontWeight.W_500),
                    ft.Row(
                        controls= [
                            ft.Text(f"{post['name']}", size= 13, color= ft.Colors.BLUE_GREY_700),
                            ft.Icon(ft.Icons.VERIFIED, size= 16, color= ft.Colors.BLUE_200),
                        ],
                        spacing= 4,
                        alignment= ft.MainAxisAlignment.START,                       
                    ),
                ],
                spacing= 6,
            ),
        )
    
    if user["verified"] == True:
        return ft.View(
            route= "/chat",

            controls= [
            ft.AppBar(
                title= ft.GestureDetector(on_tap= open_profile, content=ft.Row ( controls= [
                    ft.Text(f"{user['name']}", size= 16, weight= ft.FontWeight.BOLD),
                    #center_title= True,
                    ft.Icon(ft.Icons.VERIFIED, size= 16, color= ft.Colors.BLUE),
                ],
                spacing= 4,
                alignment= ft.MainAxisAlignment.CENTER,
                )),
                leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, tooltip="go back", on_click= to_feed),
            ),
            scroll_column,
            input_bar
            
            ]
        )
    else:
        return ft.View(
                    route= "/chat",
        
                    controls= [
                    ft.AppBar(
                        title= ft.GestureDetector(on_tap= open_profile, content=ft.Row( controls= [
                            ft.Text(f"{user['name']}", size= 16, weight= ft.FontWeight.BOLD),
                            
                        ],
                        spacing= 4,
                        alignment= ft.MainAxisAlignment.CENTER,
                        )),
                        leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, tooltip="go back", on_click= to_feed),
                    ),
                    scroll_column,
                    input_bar
                    
                    ]
                )