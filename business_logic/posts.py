from datetime import datetime, timedelta
import flet as ft


NEEDS = {
    "Event & party hire": ["chair", "cooler", "gazebo", "marquee", "speaker"],
    "Family care & check-ins": ["family member", "caregiver", "check-in", "check in", "wellness", "check-ins"],
    "Rooms & places to rent": ["room to rent", "rooms to rent", "place to rent", "rent a room", "rent a place", "somewhere to rent", "somewhere to stay", "looking for a room", "looking for a place", "backroom", "back room", "accommodation", "flat", "bachelor room", ],
}


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
             "ratings": [5, 4, 5, 2, 3, 3, 4, 5, 4, 4], 
             "help_count": 12,
             "verified": True,
             "bio": "It's ur guy Sipho"
             
             },
            {"id": 2, 
            "name": "Mama Dlamini", 
            "ratings": [5, 4, 5, 5, 4, 4], 
            "help_count": 6,
            "verified": False
            },
            {"id": 3, 
             "name": "Elizabeth (betty) Ngobe", 
             "ratings": [3, 4, 4, 5, 4, 4, 3], 
             "help_count": 7,
             "verified": True,
             "bio": "Elize_betty05 on IG"
             },
            {"id": 4, 
             "name": "Spitjo", 
             "ratings": [5, 4, 5, 3, 3, 3, 4, 5, 4, 4, 4, 3], 
             "help_count": 18,
             "verified": True
             },
            {"id": 5, 
             "name": "Bongi from the corner house", 
             "ratings": [ 5, 3, 4, 4, 5, 4, 4, 2, 3], 
             "help_count": 9,
             "verified": True,
    
             },
            {"id": 6, 
             "name": "Auntie Lindiwe", 
             "ratings": [3, 4, 5, 4, 4, 5, 4, 4, 4, 3], 
             "help_count": 10,
             "verified": False
             },
            {"id": 7, 
             "name": "Kedibone S", 
             "ratings": [ 4, 3], 
             "help_count": 2,
             "verified": False
             },
            {"id": 8, 
             "name": "Zinhle boss lady", 
             "ratings": [3, 4], 
             "help_count": 2,
             "verified": True
             },
            {"id": 9, 
             "name": "Uncle Molefe (near the clinic)", 
             "ratings": [], 
             "help_count": 0,
             "verified": False
             },
            {"id": 10, 
             "name": "Karabo P Moeng", 
             "ratings": [ 3], 
             "help_count": 1,
             "verified": False
             },

            {"id": 11, 
            "name": "Molobela Palesa", 
            "ratings": [], 
            "help_count": 8,
            "verified": False
            },
            {"id": 12, 
            "name": "Demo user", 
            "ratings": [], 
            "help_count": 0,
            "verified": False
            },
            {"id": 13, 
            "name": "Mogau Mabelane", 
            "ratings": [], 
            "help_count": 0,
            "verified": False
            },
            {"id": 14, 
            "name": "Samkelo Malepe", 
            "ratings": [], 
            "help_count": 0,
            "verified": False
            },
            {"id": 15, 
            "name": "Thulani Mathebula", 
            "ratings": [], 
            "help_count": 0,
            "verified": False
            },
            {"id": 16, 
            "name": "Tshepo Nkambule", 
            "ratings": [], 
            "help_count": 0,
            "verified": True
            },
            {"id": 17, 
            "name": "Peggy Mthembu", 
            "ratings": [], 
            "help_count": 0,
            "verified": False
            },
            {"id": 18, 
            "name": "Mandla Sibanda", 
            "ratings": [3, 2, 4, 4, 3], 
            "help_count": 5,
            "verified": False
            },

            {"id": 19, 
            "name": "Zodwa (Kelly)", 
            "ratings": [], 
            "help_count": 0,
            "verified": False,
            "bio": "I'm not for everyone"
            },
            {"id": 20, 
            "name": "David Kamo", 
            "ratings": [], 
            "help_count": 0,
            "verified": True,
            "bio": "Making Natural Science fun & easy\nGrades 4-9|CAPS aligned"
            }
            

    
        ]

        self.posts= [

            {
                "id": 1,
                "poster": 1,
                "text": "need a ladder for roof repair, can pay R60",
                "time_stamp": datetime.now() - timedelta(days= 0.2),
                "resolved": False
            },
            {
                "id": 2,
                "poster": 2,
                "text": "Hello. is anyone heading near a pharmacy today and be able to do a small pickup for me?",
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
                "text": "Can someone rent me a big cooler real quick? Need it today.",
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
                "text": "Hi... I'm looking for a backroom, budget R800",
                "time_stamp": datetime.now() - timedelta(days= 2),
                "resolved": True
            },
            {
                "id": 7,
                "poster": 7,
                "text": "does anyone have 50 plastic chairs to rent",
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
                "text": "need a room to rent. It's urgent, single person",
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
            
                "text": "looking for someone reliable to do daily check-ins",
                "time_stamp": datetime.now() - timedelta(days= 5),
                "resolved": False
                
            },
                        {
                "id": 13,
                "poster": 13,
                "text": "Yo, any1 got a gazebo to hire for Saturday?",
                "time_stamp": datetime.now() - timedelta(days= 9),
                "resolved": True
            },
            {
                "id": 14,
                "poster": 14,
                "text": "Looking for a room with own toilet and prepaid. Budget R1000-R1200",
                "time_stamp": datetime.now() - timedelta(days= 12),
                "resolved": True
            },
            {
                "id": 15,
                "poster": 15,
                "text": "pls anyone with a big cooler box??? will pay for the day",
                "time_stamp": datetime.now() - timedelta(days= 18),
                "resolved": False
            },
            {
                "id": 16,
                "poster": 16,
                "text": "looking for a caregiver for a few hours in the mornings",
                "time_stamp": datetime.now() - timedelta(days= 8),
                "resolved": True
            },
            {
                "id": 17,
                "poster": 10,
                "text": "Need 3 big coolers for this weekend, anyone got any I can rent?",
                "time_stamp": datetime.now() - timedelta(days= 10),
                "resolved": True
            },
            {
                "id": 18,
                "poster": 17,
                "text": "Hello, I'm looking for someone to do wellness visits during the day.",
                "time_stamp": datetime.now() - timedelta(days= 13),
                "resolved": False
            },
            {
                "id": 19,
                "poster": 18,
                "text": "Good morning. I am looking for a bachelor room with prepaid electricity. My budget is R1.2k",
                "time_stamp": datetime.now() - timedelta(days= 7.5),
                "resolved": True
            },
            {
                "id": 20,
                "poster": 19,
                "text": "Anyone who can rent me 30 chairs for this weekend?",
                "time_stamp": datetime.now() - timedelta(days= 11),
                "resolved": True
            },
            {
                "id": 21,
                "poster": 20,
                "text": "Anyone heading to Polokwane tomorrow?",
                "time_stamp": datetime.now() - timedelta(days= 13),
                "resolved": False
            },
            {
                "id": 22,
                "poster": 1,
                "text": "Looking for a Grade 9 maths tutor for 2 afternoons a week",
                "time_stamp": datetime.now() - timedelta(days= 19),
                "resolved": True
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

    def get_needs(self):
        now = datetime.now()
        counts = {}
        for post in self.posts + self.new_posts:
            if (now - post["time_stamp"]).total_seconds() / 86400 >= 7:
                continue
            text = post["text"].lower()
            for need, words in NEEDS.items():
                if any(w in text for w in words):
                    entry = counts.setdefault(need, {"need": need, "total": 0, "open": 0})
                    entry["total"] += 1
                    if not post.get("resolved", False):
                        entry["open"] += 1
                    break
        needs = [n for n in counts.values() if n["total"] >= 2]
        needs.sort(key=lambda n: n["total"], reverse=True)
        return needs[:3]

    def get_trends(self):
        now = datetime.now()
        trends = {}
        for post in self.posts + self.new_posts:
            text = post["text"].lower()
            for need, words in NEEDS.items():
                if any(w in text for w in words):
                    t = trends.setdefault(need, {"two_weeks_ago": 0, "last_week": 0, "this_week": 0})
                    age_days = (now - post["time_stamp"]).total_seconds() / 86400
                    if age_days < 7:
                        t["this_week"] += 1
                    elif age_days < 14:
                        t["last_week"] += 1
                    elif age_days < 21:
                        t["two_weeks_ago"] += 1
                    break
        for t in trends.values():
            change = t["this_week"] - t["last_week"]
            t["next_week"] = max(0, int(t["this_week"] + change / 2 + 0.5))
            if change > 0:
                t["tag"] = "growing"
            elif change < 0:
                t["tag"] = "slowing"
            else:
                t["tag"] = "steady"
        return trends

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


        name_controls = [ft.Text(f"{self.name}", weight=ft.FontWeight.BOLD, size=16)]
        if self.verified:
            name_controls.append(ft.Icon(ft.Icons.VERIFIED, size=16, color=ft.Colors.TEAL))

        self.content = ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(controls=name_controls, spacing=6),
                        ft.PopupMenuButton(
                            icon=ft.Icons.MORE_VERT,
                            icon_size=20,
                            tooltip="Post options",
                            items=[
                                self.helped_item,
                                ft.PopupMenuItem(
                                    icon=ft.Icons.DELETE_OUTLINE,
                                    content=ft.Text("Delete post", color=ft.Colors.RED),
                                    on_click=self.delete_post,
                                ),
                            ],
                        ),
                    ],
                ),
                ft.Container(
                    margin=10,
                    content=ft.Text(f"{self.request}", size=16, weight=ft.FontWeight.W_400),
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(f"{self.time}", size=12, color=ft.Colors.GREY_500),
                        self.helped_tag,
                    ],
                ),
            ],
        )
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


        name_controls = [ft.Text(f"{self.name}", weight=ft.FontWeight.BOLD, size=16)]
        if self.verified:
            name_controls.append(ft.Icon(ft.Icons.VERIFIED, size=16, color=ft.Colors.TEAL))

        self.content = ft.Column(
            controls=[
                ft.Row(controls=name_controls, spacing=6, alignment=ft.MainAxisAlignment.START),
                ft.Container(
                    margin=10,
                    content=ft.Text(f"{self.request}", size=16, weight=ft.FontWeight.W_400),
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(f"{self.time}", size=12, color=ft.Colors.GREY_500),
                        self.helped_tag,
                    ],
                ),
                self.help_btn,
            ],
        )
        self.padding= 12
        self.border= ft.Border.all(1, ft.Colors.OUTLINE_VARIANT)
        self.border_radius= 8


