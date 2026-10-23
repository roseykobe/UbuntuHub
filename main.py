import flet as ft
from views.login_view import login
#from views.home_view import home
from views.home_view import home
#from views.find_help_view import find_help
from views.find_help_view import find_help
from views.offer_help_view import get_paid

from views.post_form_view import post_form
from views.inbox_view import inbox
from views.chat_view import chat
from  views.find_help_chat_view import fh_chat
#from business_logic.feed import chat_preview
from business_logic.posts import chat_preview
from business_logic.fhchat import findh_chat
#from business_logic.feed import Feed
from business_logic.posts import Feed
#from business_logic.offers import Offers
from business_logic.offers import Offers
from views.profile_view import profile
from views.profile_view1 import profile1




def main( page: ft.Page): 

    page.title= "Ubuntu Hub"
    

    request_preview= chat_preview(page)
    
    fhchat= findh_chat(page)

    feed= Feed()
    offers= Offers()

    def navigation_changed(e):
            index = e.control.selected_index

            #if index== 0:
                #page.navigate("/login")
            if index == 0:
                page.navigate("/home")
    
            elif index == 1:
                page.navigate("/FindHelp")
            elif index == 2:
                 page.navigate("/GetPaid")
            elif index == 3:
                page.navigate("/analytics")
    

    def make_nav(selected_index):
        return ft.NavigationBar(
            selected_index=selected_index,
            on_change=navigation_changed,
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.HOME_OUTLINED,
                    selected_icon=ft.Icons.HOME,
                    label="Home",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.FIND_IN_PAGE_OUTLINED,
                    selected_icon=ft.Icons.FIND_IN_PAGE,
                    label="Find Help",
                ),
                ft.NavigationBarDestination(
                     icon= ft.Icons.HANDSHAKE_OUTLINED,
                     selected_icon= ft.Icons.HANDSHAKE,
                     label= "Offer Help"
                ),
                ft.NavigationBarDestination(
                    icon= ft.Icons.SHOW_CHART_OUTLINED,
                    selected_icon= ft.Icons.SHOW_CHART,
                    label= "Analytics"
                )
            ],
        )

    def route_change(e):
        page.views.clear()


    
        if page.route== "/home" :
            view= (home(page, request_preview, feed))
            view.navigation_bar= make_nav(0)
            page.views.append(view)
        elif page.route== "/FindHelp":
            view= (find_help(page, fhchat, offers))
            view.navigation_bar= make_nav(1)
            page.views.append(view)
        elif page.route== "/GetPaid":
            view= (get_paid(page, offers))
            view.navigation_bar= make_nav(2)
            page.views.append(view)
        elif page.route== "/postform":
            view= (post_form(page, feed)) 
            page.views.append(view)
        elif page.route== "/inbox":
            view= (inbox(page, request_preview, fhchat))
            page.views.append(view)
        elif page.route== "/chat":
            view= (chat(page, request_preview))
            page.views.append(view)
        elif page.route == "/fhchat":
            view = (fh_chat(page, fhchat))
            page.views.append(view)
        elif page.route == "/profile":
            view= profile(page, offers, fhchat.profile_id)
            page.views.append(view)
        elif page.route == "/profile1":
            view= profile1(page, feed, request_preview.profile_id)
            page.views.append(view)
        elif page.route== "/login" or "/":
            view= login(page)
            page.views.append(view)
        

        page.update()

    page.on_route_change= route_change
    
    route_change(None)

ft.run(main)