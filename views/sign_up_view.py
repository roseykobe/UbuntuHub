import flet as ft



def sign_up(page: ft.Page):



    return ft.View(
        route= "/signup",

        controls= [
            ft.Column(
                controls= [
                    ft.Text("UbuntuHub", size= 24, weight= ft.FontWeight.BOLD),
                    ft.Text("I am because you are", size= 16, color= ft.Colors.GREY_800,),
                    ft.Row(
                        controls=[
                            ft.Text("phone number:"),
                            ft.TextField(hint_text= "e.g. 0123456789")
                        ],
                    ),
                    ft.Row(
                        controls= [
                        ft.Text("Username: "),
                        ft.TextField(hint_text= "what do people know you as?")
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("Password: "),
                            ft.TextField("")
                        ]
                    )

                ]
            )
        ]
    )