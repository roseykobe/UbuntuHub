from datetime import datetime, timedelta
import flet as ft


class Feed:
    def __init__(self):

        self.reviews= [
            {"id": 1, "reviewer_id": 6, "stars": 5, "comment": "Is a nice guy."},
            {"id": 1, "reviewer_id": 3, "stars": 4, "comment": "Always on time."},
            {"id": 2, "reviewer_id": 4, "stars": 5, "comment": ""},
        ]
        self.reports= []


        self.users= [
            {"id": 1, 
             "name": "Sipho (Next to TK's spaza)", 
             "ratings": [5, 4, 5, 5, 3.8, 4.3, 4.8, 5, 4.5, 4, 4.2, 3.9], 
             "help_count": 12,
             "verified": True,
             
             },
            {"id": 2, 
            "name": "Mama Dlamini", 
            "ratings": [5, 4, 5, 5, 4.3, 4.8,], 
            "help_count": 6,
            "verified": False
            },
            {"id": 3, 
             "name": "Elizabeth (betty) Ngobe", 
             "ratings": [3.8, 4.3, 4.8, 5, 4.5, 4, 3.9], 
             "help_count": 7,
             "verified": True,
             "bio": "Elize_betty05 on IG"
             },
            {"id": 4, 
             "name": "Spitjo", 
             "ratings": [5, 4, 5, 5, 3.8, 4.3, 4.8, 5, 4.5, 4, 4.2, 3.9, 4, 3.5, 4.6, 3.9, 4, ], 
             "help_count": 18,
             "verified": True
             },
            {"id": 5, 
             "name": "Bongi from the corner house", 
             "ratings": [ 5, 3.8, 4.3, 4.8, 5, 4.5, 4, 4.2, 3.9], 
             "help_count": 9,
             "verified": True,
    
             },
            {"id": 6, 
             "name": "Auntie Lindiwe", 
             "ratings": [5, 4, 5, 4.3, 4.8, 5, 4.5, 4, 4.2, 3.9], 
             "help_count": 10,
             "verified": False
             },
            {"id": 7, 
             "name": "Kedibone S", 
             "ratings": [ 4.2, 3.9], 
             "help_count": 2,
             "verified": False
             },
            {"id": 8, 
             "name": "Zinhle boss lady", 
             "ratings": [3.8, 4.3, 4.8, 5], 
             "help_count": 12,
             "verified": True
             },
            {"id": 9, 
             "name": "Uncle Molefe (near the clinic)", 
             "ratings": [5, 4, 5, 3.9, 5, 3.8, 4.3, 4.8, 5, 4.5, 4, 4.2, 3.9], 
             "help_count": 13,
             "verified": False
             },
            {"id": 10, 
             "name": "Karabo P Moeng", 
             "ratings": [ 3.8, 4.3, 4.5, 4.2, 3.9], 
             "help_count": 5,
             "verified": False
             },

            {"id": 11, 
            "name": "Molobela Palesa", 
            "ratings": [5, 3.8, 4.3, 4.8, 5, 4.5, 4, 4.2], 
            "help_count": 8,
            "verified": False
            },
            {"id": 12, 
            "name": "Demo user", 
            "ratings": [], 
            "help_count": 0,
            "verified": False
            },
    
        ]

        self.posts= [

            {
                "id": 1,
                "poster": 1,
                "text": "Need a ladder for roof repair, can pay R60",
                "time_stamp": datetime.now() - timedelta(days= 0.2),
                "resolved": False
            },
            {
                "id": 2,
                "poster": 2,
                "text": "Is anyone heading near a pharmacy today and be able to do a small pickup for me?",
                "time_stamp": datetime.now() - timedelta(days= 0.8),
                "resolved": True
            },
            {
                "id": 3,
                "poster": 3,
                "text": "Seeking a reliable caregiver for a family member, approx. 2 weeks, paid. ",
                "time_stamp": datetime.now() - timedelta(days= 1),
                "resolved": False
            },
            {
                "id": 4,
                "poster": 4,
                "text": "Can someone rent me a big cooler real quick?",
                "time_stamp": datetime.now() - timedelta(days= 1),
                "resolved": False
            },
            {
                "id": 5,
                "poster": 5,
                "text": "Looking for someone to help a family member with a daily routine/check-ins. Please DM if you have experience and availability",
                "time_stamp": datetime.now() - timedelta(days= 2),
                "resolved": False
            },
            {
                "id": 6,
                "poster": 6,
                "text": "There's a stranger hanging around my gate. I'm not sure if it's nothing or something, but could a few of you come check it out?",
                "time_stamp": datetime.now() - timedelta(days= 2),
                "resolved": True
            },
            {
                "id": 7,
                "poster": 7,
                "text": "Looking for 50 plastic chairs to rent",
                "time_stamp": datetime.now() - timedelta(days= 3),
                "resolved": False
            },
            {
                "id": 8,
                "poster": 8,
                "text": "Can someone help me fix my fence? it got knocked down by the wind last night",
                "time_stamp": datetime.now() - timedelta(days= 3),
                "resolved": True
            },
            {
                "id": 9,
                "poster": 9,
                "text": "Need help loading wood, I'll share some if you help",
                "time_stamp": datetime.now() - timedelta(days= 3),
                "resolved": True
            },
            {
                "id": 10,
                "poster": 3,
                "text": "Is anyone available for a quick wellness check on a family member this afternoon near Zone 3?",
                "time_stamp": datetime.now() - timedelta(days= 4),
                "resolved": True
            },
            {
                "id": 11,
                "poster": 10,
                "text": "Need 7 kids' chairs, i can come pick them up",
                "time_stamp": datetime.now() - timedelta(days= 5),
                "resolved": False
            },
            {
                "id": 12,
                "poster": 11,
                "text": "Need a 3 big coolers for this weekend, anyone got any I can rent?",
                "time_stamp": datetime.now() - timedelta(days= 5),
                "resolved": False
                
            }
        ]

        self.new_posts= []

    def get_user(self, user_id):
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None
    
    def add_post(self, user_id, text):
        self.posts.append({"id": len(self.posts) + 1,
                              "poster": user_id,
                              "text": text,
                              "time_stamp": datetime.now()}),

    #def to_feed(self, text):
        #self.new_posts.append({
            #"id": len(self.posts) + 1,
            #"poster": 12,
            #"text": text,
            #"time_stamp": datetime.now(),
            #"resolved": False
        #})

    def to_feed(self, text):
        new_id = 1
        for p in self.posts + self.new_posts:
            if p["id"] >= new_id:
                new_id = p["id"] + 1

        self.new_posts.append({
            "id": new_id,
            "poster": 12,
            "text": text,
            "time_stamp": datetime.now(),
            "resolved": False
        })



    def time_ago(self, time_stamp):
        seconds= (datetime.now()- time_stamp).total_seconds()
        if seconds <3600:
            return f"{int(seconds//60)}m ago"
        if seconds < 86400:
            return f"{int(seconds//3600)}h ago"
        return f"{int(seconds//86400)}d ago"

    
    
    def get_rating(self, helper_id):
        user = self.get_user(helper_id)
        if user is None:
            return 0, 0
        ratings = user.get("ratings", [])
        if not ratings:
            return 0, 0
        return sum(ratings) / len(ratings), len(ratings)

    def get_reviews(self, helper_id):
            result = []
            for r in self.reviews:
                if r["id"] == helper_id:
                    result.append(r)
    
            result.reverse()  # newest first
            return result
    

    def add_review(self, helper_id, stars, comment):
        user = self.get_user(helper_id)
        if user is None:
            return
        user.setdefault("ratings", []).append(stars)
        self.reviews.append({
            "id": helper_id,
            "reviewer_id": 12,
            "stars": stars,
            "comment": comment.strip()
        })

    def has_reviewed(self, helper_id):
            
            for r in self.reviews:
                if r["id"]== helper_id and r["reviewer_id"] == 12:
                    return True
            return False
    def add_report(self, helper_id, reason):
            self.reports.append({
                "id": helper_id,
                "reporter_id": 12,
                "reason": reason
            })

    



def get_feed():
    feed= []
    posts= Feed()
    newest_first= sorted(posts.posts, key= lambda p: p["time_stamp"], reverse=True)

    for post in newest_first:
        
        user= posts.get_user(post["poster"])
        
        name= user["name"] if user else "unknown"
        
        feed.append({**post, "name": name})
        
        #time_posted= time_ago(post["time_stamp"])
        #print(name, post["text"], time_posted)

    return feed




class chat_preview:
    def __init__(self, page):
        self.page=page
    
        self.selected=None
    

    def deliver(self, e):
        
        
        if self.selected is None:
            self.page.navigate("/home")

        self.selected= e.control.data
        

        self.page.navigate('/chat')


class newPostCard(ft.Container):
    def __init__(self, name, request, time, verified, chat_preview, object, posts_list= None):
        super().__init__()
        self.name= name
        self.request= request
        self.time= time 
        self.verified= verified
        self.chat_preview= chat_preview
        self.object= object

        self.posts_list= posts_list
        self.post= self.object[1]

        resolved= self.post.get('resolved', False)

        self.helped_tag= ft.Container(
            visible= resolved,
            bgcolor=ft.Colors.GREEN_50,
            border_radius=10,
            padding= ft.Padding(left= 8, right=8, top=2, bottom=2),
            content= ft.Text("Helped ✓", size= 11, color= ft.Colors.GREEN_700),
        )
        self.helped_item= ft.PopupMenuItem(
            icon= ft.Icons.CHECK_CIRCLE_OUTLINE,
            content= ft.Text("Mark as not helped" if resolved else "Mark as helped"),
            on_click= self.toggle_helped,
        )


        if self.verified:
            self.content= ft.Column(
                        controls= [
                            ft.Row(
                                alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment= ft.CrossAxisAlignment.CENTER,
    
                                controls= [ ft.Row(
                                           controls= [
                                    ft.Text(f"{self.name}", weight= ft.FontWeight.BOLD, size= 16),
                                    ft.Icon(ft.Icons.VERIFIED, size= 16, color= ft.Colors.ORANGE_200),
                                ],
                                spacing= 6,
                            ),
                            ft.PopupMenuButton(
                                icon= ft.Icons.MORE_VERT,
                                icon_size= 20,
                                tooltip= "Post options",
                                items= [
                                    ft.PopupMenuItem(
                                        icon= ft.Icons.CHECK_CIRCLE_OUTLINE,
                                        content= ft.Text("Mark as helped"),
                                        on_click= self.toggle_helped,
                                    ),
                                    ft.PopupMenuButton(
                                        icon= ft.Icons.DELETE_OUTLINE,
                                        content= ft.Text("Delete post", color= ft.Colors.RED),
                                        on_click= self.delete_post,
                                    ),
                                ],
                            ),
                                ],
                                #alignment= ft.MainAxisAlignment.START,
                            ),
                            ft.Row(
                                controls= [
                                    #ft.Icon(ft.Icons.STAR, size= 14, color= ft.Colors.ORANGE),
                                    #ft.Text(f"{self.rating} ({self.help_count} helps)",  size= 12, color= ft.Colors.GREY_600)
                                ],
                                spacing= 4,
                            ),
                            ft.Container(
                                margin= 10, 
                                content= ft.Text(
                                    f"{self.request}",
                                    size=16, 
                                    weight= ft.FontWeight.W_400,
                                ),
                            ),
                            ft.Text(f"{self.time}", size= 12, color=ft.Colors.GREY_500),
            
                        ])
        else:
            self.content= ft.Column(
                        controls= [
                            ft.Row(
                                alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment= ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Row( controls= [
                                    ft.Text(f"{self.name}", weight= ft.FontWeight.BOLD, size= 16),
                                    self.helped_tag,
                                    ],
                                    spacing= 6
                                    ),
                                    ft.PopupMenuButton(
                                                                    icon= ft.Icons.MORE_VERT,
                                                                    icon_size= 20,
                                                                    tooltip= "Post options",
                                                                    items= [
                                                                        self.helped_item,
                                                                        ft.PopupMenuItem(
                                                                            icon= ft.Icons.DELETE_OUTLINE,
                                                                            content= ft.Text("Delete post", color= ft.Colors.RED),
                                                                            on_click= self.delete_post,
                                                                        ),
                                                                    ],
                                                                ),
                                ],
                                
                                #alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                                #vertical_alignment= ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Row(
                                controls= [
                                    #ft.Icon(ft.Icons.STAR, size= 14, color= ft.Colors.ORANGE),
                                    #ft.Text(f"{self.rating} ({self.help_count} helps)",  size= 12, color= ft.Colors.GREY_600)
                                ],
                                spacing= 4,
                            ),
                            ft.Container(
                                margin= 10, 
                                content= ft.Text(
                                    f"{self.request}",
                                    size=16, 
                                    weight= ft.FontWeight.W_400,
                                ),
                            ),
                            ft.Text(f"{self.time}", size= 12, color=ft.Colors.GREY_500),
            
                            #ft.Container(
                                
                                #width= 130,
                                #data= self.object, 
                                #height= 40,
                                #bgcolor= ft.Colors.ORANGE_600,
                                #border_radius= 4, 
                                #content= ft.Row(
                                    #controls= [
                                #ft.Text(
                                    #"I can help",
                                    #color= ft.Colors.WHITE,
                                    #size= 14, 
                                    #data= [self.object, self.pagey],
                                
                                    #weight= ft.FontWeight.W_500),
                                    #],
                                    #alignment= ft.MainAxisAlignment.CENTER,
                                    #spacing=0,
                                #),
                                    #ink= True,
                                    #on_click= self.chat_preview.deliver,
                                #)
                            #)
                        ])
        self.padding= 12
        self.border= ft.Border.all(1, ft.Colors.OUTLINE_VARIANT)
        self.border_radius= 8

    def toggle_helped(self, e):
        resolved = not self.post.get("resolved", False)
        self.post["resolved"] = resolved

        self.helped_tag.visible = resolved
        self.helped_item.content = ft.Text(
        "Mark as not helped" if resolved else "Mark as helped"
        )
        self.update()

    def delete_post(self, e):
        page = e.page

        def yes(ev):
        # Remove it from new_posts, whichever of the two it holds
            if self.posts_list is not None:
                for item in (self.object, self.post):
                    if item in self.posts_list:
                        self.posts_list.remove(item)
                        break
            self.visible = False
            page.pop_dialog()
            page.update()

        def no(ev):
            page.pop_dialog()

        page.show_dialog(
            ft.AlertDialog(
            modal=True,
            title=ft.Text("Delete this post?"),
            content=ft.Text(self.request),
            actions=[
                ft.TextButton("Cancel", on_click=no),
                ft.TextButton(
                    "Delete",
                    on_click=yes,
                    style=ft.ButtonStyle(color=ft.Colors.RED),
                ),
            ],
        )
    )


class PostCard(ft.Container):
    def __init__(self, name, request, time, verified, chat_preview, object):
        super().__init__()
        self.name= name
        self.request= request
        self.time= time
        
        self.verified= verified
        self.chat_preview= chat_preview
        self.object= object


        self.post = self.object[1]
        resolved = self.post.get("resolved", False)

        self.helped_tag = ft.Container(
            visible=resolved,
            bgcolor=ft.Colors.GREEN_50,
            border_radius=10,
            padding=ft.Padding(left=8, right=8, top=2, bottom=2),
            content=ft.Text("Helped ✓", size=11, color=ft.Colors.GREEN_700),
        )

        self.help_btn = ft.Container(
                                        
                                        width= 130,
                                        data= self.object, 
                                        height= 40,
                                        bgcolor= ft.Colors.ORANGE_100 if resolved else ft.Colors.ORANGE_600,
                                        border_radius= 4, 
                                        content= ft.Row(
                                            controls= [
                                        ft.Text(
                                            "I can help",
                                            color= ft.Colors.ORANGE_900 if resolved else ft.Colors.WHITE,
                                            size= 14,  
                                            weight= ft.FontWeight.W_500),
                                            ],
                                            alignment= ft.MainAxisAlignment.CENTER,
                                            spacing=0,
                                        ),
                                            ink= True,  
                                            on_click= self.chat_preview.deliver,
                                        )


        if self.verified:
            self.content= ft.Column(
                        controls= [
                            ft.Row(
                                controls=[
                                    ft.Text(f"{self.name}", weight= ft.FontWeight.BOLD, size=16),
                                    ft.Icon(ft.Icons.VERIFIED, size= 16, color= ft.Colors.BLUE_50),
                                    self.helped_tag,
                                ],
                                spacing= 6,
                                alignment= ft.MainAxisAlignment.START,
                            ),
                            ft.Row(
                                controls= [
                                    #ft.Icon(ft.Icons.STAR, size= 14, color= ft.Colors.ORANGE),
                                    #ft.Text(f"{self.rating} ({self.help_count} helps)",  size= 12, color= ft.Colors.GREY_600)
                                ],
                                spacing= 4,
                            ),
                            ft.Container(
                                margin= 10, 
                                content= ft.Text(
                                    f"{self.request}",
                                    size=16, 
                                    weight= ft.FontWeight.W_400,
                                ),
                            ),
                            ft.Text(f"{self.time}", size= 12, color=ft.Colors.GREY_500),
                            self.help_btn,
                        ])
        else:
            self.content= ft.Column(
                        controls= [
                            ft.Row(
                                controls=[
                                    ft.Text(f"{self.name}", weight= ft.FontWeight.BOLD, size= 16),
                                    self.helped_tag,
                                ],
                                spacing= 6,
                                alignment= ft.MainAxisAlignment.START,
                            ),
                            ft.Row(
                                controls= [
                                    #ft.Icon(ft.Icons.STAR, size= 14, color= ft.Colors.ORANGE),
                                    #ft.Text(f"{self.rating} ({self.help_count} helps)",  size= 12, color= ft.Colors.GREY_600)
                                ],
                                spacing= 4,
                            ),
                            ft.Container(
                                margin= 10, 
                                content= ft.Text(
                                    f"{self.request}",
                                    size=16, 
                                    weight= ft.FontWeight.W_400,
                                ),
                            ),
                            ft.Text(f"{self.time}", size= 12, color=ft.Colors.GREY_500),
            
                            self.help_btn,
                            #)
                        ])
        self.padding= 12
        self.border= ft.Border.all(1, ft.Colors.OUTLINE_VARIANT)
        self.border_radius= 8


