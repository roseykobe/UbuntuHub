import flet as ft
#from business_logic.feed import PostCard
from business_logic.posts import PostCard
#from business_logic.feed import Feed
from business_logic.posts import Feed
import asyncio




def post_form (page: ft.Page, feed: Feed):


    async def submit_post(e):
        print(post_field.value, "submitted")

        #async def load_before_submit():
        loader= ft.Container(
            content= ft.ProgressRing(),
            alignment= ft.Alignment.CENTER,
            expand= True,
            bgcolor= ft.Colors.with_opacity(0.4, ft.Colors.BLACK)
        )
        page.overlay.append(loader)
        page.update()
        
        await asyncio.sleep(1.5)
        page.overlay.remove(loader)
        

        feed.to_feed(post_field.value)
        post_field.value= ""
        post_btn.disabled= True

        page.show_dialog(
             ft.SnackBar(
                  ft.Text("Posted successfully."),
                  duration= 800,
                  behavior= ft.SnackBarBehavior.FLOATING,
                  margin= ft.Margin.only(bottom= 100, left=20, right= 20),
             )
        )
        page.navigate("/home")

        page.update()


    post_btn= ft.FilledButton("POST", bgcolor= ft.Colors.ORANGE, color= ft.Colors.WHITE, height= 46, disabled= True, on_click= submit_post, expand= True,)


    def check_field(e):
        post_btn.disabled= not post_field.value.strip()
        page.update()

    post_field=ft.TextField(
        hint_text= "e.g. 'Need help moving furniture' ",
        hint_style= ft.TextStyle(color= ft.Colors.GREY_600),
        filled= True,
        multiline=True,
        on_change= check_field,
        max_length= 150,
        bgcolor= ft.Colors.WHITE,
        color= ft.Colors.BLACK,
        border_radius= 12,
        border_color= ft.Colors.ORANGE_300,
        focused_border_color= ft.Colors.ORANGE,
        min_lines= 3,
        max_lines= 5,
    )


    def go_home():
        page.navigate("/home")




    page.update()
    return ft.View(
        route= "/postform",

        controls= [
            ft.AppBar(
                title= ft.Text("Post to the feed"),
                center_title= True,
                leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, tooltip="go back", on_click= go_home),
            ),
            ft.Column (
                scroll= ft.ScrollMode.AUTO,
                expand= True,

                controls= [
                    #ft.Container(
                        #padding= 12, 
                        #margin= 10,
                        #bgcolor= ft.Colors.ORANGE_100,
                        #border_radius= 8,
                        #content= ft.Text(
                            #"Post as Demo User",
                            #size= 13,
                            #color= ft.Colors.ORANGE_800,
                        #),
                    #),
                    ft.Container (
                        width= page.width - 30,
                        padding= 16, 
                        bgcolor= ft.Colors.ORANGE_50,
                        border_radius=16,
                        margin= ft.Margin.only(left= 12, right= 12),
                        content= ft.Column(
                            horizontal_alignment= ft.CrossAxisAlignment.STRETCH,
                            controls= [
                                ft.Text("What do you need help with?", size= 14, color= ft.Colors.ORANGE_900),
                                post_field,
                                ft.Text ('Posting as Demo User', size= 12, color= ft.Colors.GREY_600),
                                ft.Row(controls= [
                                    #ft.Container (width= 60),
                                    post_btn]),
                                #ft.Icon(icon= ft.Icons.LOCK, size= 16, color= ft.Colors.GREY_500),
                            ],
                            spacing= 10
                        )
                    )
                ]
            )
        ]
    )