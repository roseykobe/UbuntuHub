import flet as ft
from business_logic.posts import PostCard
#from business_logic.feed import newPostCard
from business_logic.posts import newPostCard
from business_logic.posts import chat_preview 
#from business_logic.feed import Feed
from business_logic.posts import Feed


def home(page: ft.Page, request_preview: chat_preview, feed: Feed):


    def go_to_postform(e):
            page.navigate("/postform")
    
    def go_to_messages(e):
            page.navigate("/inbox")


    post_cards= []
    def create_cards():
        for post in reversed(feed.new_posts):
            user= feed.get_user(post["poster"])
            newpostcard= newPostCard(
            name= user["name"],
            request= post["text"],
            time= feed.time_ago(post["time_stamp"]),
            verified= user["verified"],
            chat_preview= request_preview,
            object= [user, post],
            posts_list= feed.new_posts
        
            )
            post_cards.append(newpostcard)
        for post in feed.posts:
            user= feed.get_user(post["poster"])
            postcard= PostCard(
                name= user["name"],
                request= post["text"],
                time= feed.time_ago(post["time_stamp"]),
                verified= user["verified"],
                chat_preview= request_preview,
                object= [user, post]

            )
            post_cards.append(postcard)
        page.update()

    create_cards()
        
    return ft.View(
            route= "/home",
    
            controls= [
                ft.AppBar(
                    title= ft.Text("UbuntuHub", weight= ft.FontWeight.BOLD, font_family="Montserrat",),
                    actions= [
                        ft.IconButton(icon=ft.Icons.ADD_CIRCLE, tooltip="post", on_click= go_to_postform),
                        ft.IconButton(icon= ft.Icons.MESSAGE, tooltip= "messages", on_click= go_to_messages)
                    ]
                ),
                ft.Text("See who needs help"),
                ft.Column(
                    scroll= ft.ScrollMode.AUTO,
                    expand= True,
    
                    controls=[ *post_cards]
                )
            ]
        )