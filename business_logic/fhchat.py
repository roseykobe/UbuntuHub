import flet as ft


class findh_chat:
    def __init__(self, page):
        self.page= page

        self.selected= None

    def to_chat(self, info):

        #print(info, "info")
        name= info["name"]
        verified= info["verified"]
        offer_title= info["title"]
        

        header= [ft.Text(name, weight= ft.FontWeight.BOLD)]
        if verified:
            header.append(ft.Icon(icon= ft.Icons.VERIFIED, color= ft.Colors.BLUE, size=18))
        #post= data
        #post_list= post.split("-")
        #name= post_list[0]
        #post_list.pop(0)
        #offer= "-".join(post_list)

    
        if self.selected is None:
            self.page.navigate("/FindHelp")

        
        self.selected= {
            "name": name,
            "offer": offer_title,
            "header": header,
            'helper_id':info["helper_id"]
        }
        self.page.navigate("/fhchat")

