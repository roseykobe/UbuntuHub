import flet as ft



def login (page: ft.Page):

    

    def logged_in(e):
        page.navigate("/home")

    login_form= ft.Column(
                    expand= True,
                    controls= [
                        ft.Text("UbuntuHub", size= 24, weight= ft.FontWeight.BOLD),
                        ft.Text("I am because we are", size= 16, color= ft.Colors.GREY_800),
                        ft.TextField(label= "email", value= "demo_user@gmail.com", filled= True,),
                        ft.TextField(label= "password", value= "demo_user123", filled= True, password=True,  can_reveal_password=True),
                        ft.FilledButton("log in", on_click= logged_in),
    
                    ],
                    alignment= ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER
    )



    return ft.View(
        route= "/login",

        controls= [
            ft.Row(
                expand= True,
                controls= [
                    login_form
                ],
                alignment= ft.MainAxisAlignment.CENTER,
                vertical_alignment= ft.CrossAxisAlignment.CENTER,
            )
        ]
    )