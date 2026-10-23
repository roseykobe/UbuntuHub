import flet as ft


class Offers:
    def __init__(self):
        
        self.reviews= [
            {"helper_id": 1, "reviewer_id": 66, "stars": 5, "comment": "Explained fractions so well."},
            {"helper_id": 1, "reviewer_id": 67, "stars": 4, "comment": "Always on time."},
            {"helper_id": 2, "reviewer_id": 68, "stars": 5, "comment": ""},
        ]
        self.reports= []
        self.paid_categories= {
            "tutoring": {"name": "Tutoring", "icon": ft.Icons.BOOK, "color": ft.Colors.RED},
            "hair": {"name": "Hair & Grooming", "icon": ft.Icons.CONTENT_CUT, "color": ft.Colors.ORANGE},
            "tools": {"name": "Tools for Hire", "icon": ft.Icons.HANDYMAN, "color": ft.Colors.GREY},
            "gardening": {"name": "Gardening", "icon": ft.Icons.SPA, "color": ft.Colors.GREEN},
            "laundry": {"name": "Laundry", "icon": ft.Icons.LOCAL_LAUNDRY_SERVICE, "color": ft.Colors.BLUE_GREY},
            "veggies": {"name": "Veggies", "icon": ft.Icons.ECO, "color": ft.Colors.GREEN_800},
            "baked": {"name": "Baked Goods", "icon": ft.Icons.LOCAL_CAFE, "color": ft.Colors.ORANGE_300},
            "repairs": {"name": "Repairs", "icon": ft.Icons.BUILD, "color": ft.Colors.DEEP_ORANGE},
            "charging": {"name": "Phone Charging", "icon": ft.Icons.BATTERY_CHARGING_FULL, "color": ft.Colors.YELLOW_800},
            "sewing": {"name": "Sewing & Repairs", "icon": ft.Icons.TEXTURE, "color": ft.Colors.PINK_200},
            "rides": {"name": "Rides & Delivery", "icon": ft.Icons.DIRECTIONS_BIKE, "color": ft.Colors.BLUE_600}
        }

        self.free_categories= {
            "clothes": {"name": "Clothes", "icon": ft.Icons.CHECKROOM, "color": ft.Colors.INDIGO_300},
            "food": {"name": "Food Pantry", "icon": ft.Icons.FOOD_BANK, "color": ft.Colors.AMBER_800},
            "toiletries": {"name": "Toiletries", "icon": ft.Icons.BATHROOM, "color": ft.Colors.CYAN_100},
            "school": {"name": "School Supplies", "icon": ft.Icons.BACKPACK, "color": ft.Colors.BLUE_200},
            "appliances": {"name": "Appliances", "icon": ft.Icons.HOME_REPAIR_SERVICE, "color": ft.Colors.GREY_400},
            "furniture": {"name": "Furniture", "icon": ft.Icons.CHAIR, "color": ft.Colors.BROWN_300},
            "electronics": {"name": "Electronics", "icon": ft.Icons.DEVICE_UNKNOWN, "color": ft.Colors.PURPLE_300},
            "kids": {"name": "Baby & Kids", "icon": ft.Icons.BABY_CHANGING_STATION, "color": ft.Colors.PINK_200},
            "tutoring": {"name": "Tutoring", "icon": ft.Icons.BOOK, "color": ft.Colors.RED},
        }

        self.users= {
            1: {"name": "Dimpho Makofane", "verified": True, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 3.8, 4, 4.6, 4.2, 5], "bio": "Gr12 Maths and Science Tutor\nTests, homework & exam prep\nonline & physical"},
            2: {"name": "Mandla Sibanda", "verified": False, "ratings": [3.5, 3.2, 4.2, 4.6, 3.8]},
            3: {"name": "Nomsa", "verified": False, "ratings": [4,3.5, 4.2, 4.8]},
            4: {"name": "David Kamo", "verified": True, "ratings": [4, 3.5, 5, 4.2, 4.8, 4.9, 4.8, 4.2, 4.5], "bio": "Making Natural Science fun & easy\nGrades 4-9|CAPS aligned"},
            5: {"name": "Kearabetswe", "verified": True, "ratings": [4,3.5, 4.2, 3.8]},
            6: {"name": "Sanele", "verified": False, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 3.8], "bio": "Barber| Fades, Tapers, & Lineups"},
            7: {"name": "Tebogo (Oupa)", "verified": True, "ratings": [4,3.5, 4.2, 4.8, 3.8]},
            8: {"name": "Linda's Beauty Shop", "verified": True, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 4.8], "bio": "Luxury Weaves & Bundles\nRaw, Peruvian, & Brazilian\nDm for price list"},
            9: {"name": "Sibusiso Mokoena", "verified": False, "ratings": []},
           10: {"name": "Nomfundo", "verified": True, "ratings": []},
           11: {"name": "Ntate Patric", "verified": True, "ratings": [4,3.5, 5, 3.8]},
            12: {"name": "Thandi", "verified": False, "ratings": [4,3.5, 5, 4.2, 4.1, 4.2, 3.8]},
            13: {"name": "Bongani Bongs", "verified": True, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 4.8, 5, 4.4], "bio": "Gardener| Lawns, Trimming & Clean-ups\nWeekly & once off"},
            14: {"name": "Sbu Dumane", "verified": False, "ratings": [4,3.5, 5, 4.2, 3.8]},
            15: {"name": "Cindy M", "verified": True, "ratings": [4,3.5, 5, 4.2, 4.8, 4.6, 3.8, 4, 4,3, 3,9, 4,7], "bio": "Landscaping & Garden Design\nDesign | Install | Maintain"},
            16: {"name": "Mahlaku", "verified": False, "ratings": [4,3.5, 3.6, 3.8]},
            17: {"name": "Malebo", "verified": True, "ratings": [4,3.5, 4.2, 4.8, 4.9, 3.8, 4, 3.9], "bio":"Laundry Services\nWash & Iron | Pickup & Delivery"},
            18: {"name": "Zodwa(Kelly)", "verified": True, "ratings": []},
            19: {"name": "Auntie Nomusa", "verified": False, "ratings": [4,3.5, 4.2, 4.8, ]},
            20: {"name": "Kamogelo", "verified": True, "ratings": [4, 4.2, 4.8, 4.9, 3.8], "bio": "Fresh veggies | Delivery available"},
            21: {"name": "Nomthandazo S", "verified": False, "ratings": []},
            22: {"name": "Bongi", "verified": False, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 3.8, 4, 3.6, 3.7, 4.3, 4.2], "bio": "Farm fresh eggs\nTray from R65 | Half tray from R35"},
            23: {"name": "Madimpho Tracy", "verified": True, "ratings": [ 3.1, 3.9, 4.3, 4.4, 3.7, 4.1]},
            24: {"name": "Kabelo Morena", "verified": True, "ratings": [4,3.5, 4.2, 4.8, 4.9, 3.8]},
            25: {"name": "Khutso's Delicacy", "verified": True, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 3.8, 4.3, 4.8, 3.2, 4.6], "bio": "Your Cake Plug\nBirthday cakes, cupcakes & treats\nkhutso_delicacy on IG | DM for prices"},
            26: {"name": "Noluthando", "verified": False, "ratings": [3.2, 3.3, 3.1, 3.8, 3.3, 3.8]},
            27: {"name": "Magiftana Gift", "verified": False, "ratings": []},
            28: {"name": "Tiishetso", "verified": True, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 3.8, 3.9, 4, 4.2]},
            29: {"name": "Dumisani", "verified": False, "ratings": [4,3.5, 4.2, 4.8, 3.8]},
            30: {"name": "Uncle Matthew", "verified": False, "ratings": [4,3.5, 2, 4.2]},
            31: {"name": "Pebetsi", "verified": True, "ratings": [4,3.5, 5, 4.2,]},
            32: {"name": "Karabo's spaza", "verified": True, "ratings": [4,3.5, 3.9, 4.2, 4.8, 4.2, 3.8, 4.3]},
            33: {"name": "Mathapelo (Ivy)", "verified": True, "ratings": []},
            34: {"name": "Mbali (near clinic)", "verified": True, "ratings": [4,3.5, 4.2, 4.8, 4.9, 3.8]},
            35: {"name": "Nkosi Mokwena", "verified": True, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 3.8, 4.6, 3.9, 4,8, 4.1, 4.6, 4.9, 5, 5, 4.4, 4.2], "bio": "I design & make dresses, traditional wear & more\nBring your style or I design for you\nIG: nkosi_designs08"},
            36: {"name": "Oratile", "verified": False, "ratings": []},
            37: {"name": "Mr Alpha", "verified": False, "ratings": [4,3.5, 3.5, 4.2, 4.1, 4, 3.8]},                 
            38: {"name": "Isaac Mankaba", "verified": True, "ratings": [4,3.5, 5]},
            39: {"name": "Zodwa (Kelly)", "verified": False, "ratings": [], "bio": "I'm not for everyone"},
            40: {"name": "Onalenna", "verified": True, "ratings": [4,3.5, 3.3], "bio": "God is good"},
            41: {"name": "Thabo Zakusa", "verified": False, "ratings": [4,3.5, 5, 4.2, 3.8]},
            42: {"name": "Molebogeng", "verified": False, "ratings": []},
            43: {"name": "Nomalanga Mthembu", "verified": False, "ratings": []},
            44: {"name": "Mama Dlamini", "verified": False, "ratings": [5, 4, 5, 5, 4.3, 4.8]},
            45: {"name": "Malebo", "verified": True, "ratings": [4,3.5, 3.8], "bio": "Passionate about learning, growing & helping others"},
            46: {"name": "Selina Phelane", "verified": False, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 3.8]},
            47: {"name": "Hope Komana", "verified": False, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 3.8]},
            48: {"name": "Thabsile", "verified": False, "ratings": []},
            49: {"name": "Amogelang M", "verified": False, "ratings": [4,3.5, 3.8]},
            50: {"name": "Lerato Malepe", "verified": False, "ratings": [ 4.2, 2.8, 4.1, 3.8]},
            51: {"name": "Omphemetse Madiba", "verified": True, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 3.8, 3.8, 4.6], "bio": "Passionate about helping others and building connections"},
            52: {"name": "Thandeka", "verified": False, "ratings": [4,4.2, ]},
            53: {"name": "Refilwe Molobela", "verified": True, "ratings": []},
            54: {"name": "Keneilwe S", "verified": False, "ratings": []},
            55: {"name": "Phomelelo Lelo", "verified": True, "ratings": [4,3.5,4.2, 4.8, 4, 3.8], "bio": "Hi, I'm Phomelelo Mavimbela\nI create, share, and help my community."},
            56: {"name": "Mandisa Selepe", "verified": False, "ratings": [4,3.5, 5, 4.2]},
            57: {"name": "Sandile", "verified": False, "ratings": []},
            58: {"name": "Nkosi Khona", "verified": False, "ratings": [4.1, 3.5, 3.8]},
            59: {"name": "Putinyana", "verified": True, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 3.8]},
            60: {"name": "Soka Mokonyane", "verified": False, "ratings": []},
            61: {"name": "Moloko S", "verified": False, "ratings": [3.8]},
            62: {"name": "Adelaide Mphego", "verified": False, "ratings": []},
            63: {"name": "Candice Maahlo", "verified": True, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 3.8, 4.1, 4.7, 3.9, 4, 5, 4.9, 3.8, 4.1], "bio": "Helping learners love Maths again\nGrades 8-9 | online lessons" },
            64: {"name": "Antonette", "verified": True, "ratings": [4,3.5, 5, 4.2, 4.8, 4.9, 3.8]},
            65: {"name": "Demo user", "verified": False, "ratings": []},
            66: {"name": "Mokgadi Phala", "verified": False, "ratings": []},
            67: {"name": "Phetolo Sebake", "verified": False, "ratings": []},
            68: {"name": "Angel Selahle", "verified": True, "ratings": [4, 3, 5,2,4]} 
        }

        self.paid_offers= [
            {"offer_id":1, "helper_id":1, "category": "tutoring",
             "title": "Gr12 Maths & Science, R60/hr",
             "mentorship": True
            },
            {"offer_id":2, "helper_id":2, "category": "tutoring",
            "title": "Gr4-7 English & Reading, R50/hr",
            "mentorship": False
                        },
            {"offer_id":3, "helper_id":3, "category": "tutoring",
            "title": "Matric Revision (Maths & Science), 40/hr",
            "mentorship": False
                        },
            {"offer_id":4, "helper_id":4, "category": "tutoring",
            "title": "Gr4-9 Natural Science, R35/hr",
            "mentorship": True
                        },
            {"offer_id":5, "helper_id":5, "category": "hair",
            "title": "Braids & cornrows, from R120",
            "mentorship": False
                        },
            {"offer_id":6, "helper_id":6, "category": "hair",
            "title": "Men's fades and beard trim, R80",
            "mentorship": False
                                    },
            {"offer_id":7, "helper_id":7, "category": "hair",
            "title": "cuts from R50",
            "mentorship": False
                                    },
            {"offer_id":8, "helper_id":8, "category": "hair",
            "title": "Weaves & extensions, from R200",
            "mentorship": False
                                    },
            {"offer_id":9, "helper_id":9, "category": "tools",
            "title": "Generator, R150/night",
            "mentorship": False
                                    },
            {"offer_id":10, "helper_id":10, "category": "tools",
            "title": "Power drill, R50/h",
            "mentorship": False
                                    },
            {"offer_id":11, "helper_id":11, "category": "tools",
            "title": "ladder for rent, R100/day",
            "mentorship": False
                                    },
            {"offer_id":12, "helper_id":12, "category": "gardening",
            "title": "Garden cleanup and weeding, R150/session",
            "mentorship": False
                                    },
            {"offer_id":13, "helper_id":13, "category": "gardening",
            "title": "Lawn mowing & Trimming",
            "mentorship": False
                                    },
            {"offer_id":14, "helper_id":14, "category": "gardening",
            "title": "Weeding, fertilizing, watering & plant care",
            "mentorship": False
                                    },
            {"offer_id":15, "helper_id":15, "category": "gardening",
            "title": "Landscaping & garden design",
            "mentorship": False
                                    },
            {"offer_id":16, "helper_id":16, "category": "gardening",
            "title": "Plant & pot delivery, from R120(excludes setup)",
            "mentorship": False
                                    },
            {"offer_id":17, "helper_id":17, "category": "laundry",
            "title": "Wash & iron, R120 per load",
            "mentorship": False
                                    },
            {"offer_id":18, "helper_id":18, "category": "laundry",
            "title": "Sneaker washing",
            "mentorship": False
                                    },
            {"offer_id":19, "helper_id":19, "category": "laundry",
            "title": "Bedding & blankets / duvets, R150 per set",
            "mentorship": False
                                    },
            {"offer_id":20, "helper_id":20, "category": "veggies",
            "title": "Spinach & beetroot & potatoes",
            "mentorship": False
                                    },
            {"offer_id":21, "helper_id":21, "category": "veggies",
            "title": "Tomatoes & onions, R20",
            "mentorship": False
                                    },
            {"offer_id":22, "helper_id":22, "category": "veggies",
            "title": "Fresh eggs, R2 each",
            "mentorship": False
                                    },
            {"offer_id":23, "helper_id":23, "category": "baked",
            "title": "Banana bread & rolls",
            "mentorship": False
                                    },
            {"offer_id":24, "helper_id":24, "category": "baked",
            "title": "Vetkoek with mince, R4 each",
            "mentorship": False
                                    },
            {"offer_id":25, "helper_id":25, "category": "baked",
            "title": "Cakes, from R250",
            "mentorship": True
                                    },
            {"offer_id":26, "helper_id":26, "category": "baked",
            "title": "Muffins (blueberry or chocolate), R6 each",
            "mentorship": False
                                    },
            {"offer_id":27, "helper_id":27, "category": "baked",
            "title": "Savoury pies, R20 each",
            "mentorship": False
                                    },
            {"offer_id":28, "helper_id":28, "category": "baked",
            "title": "Scones & biscuits",
            "mentorship": False
            },
            {"offer_id":29, "helper_id":29, "category": "repairs",
            "title": "Ceiling leaks, gutter cleaning",
            "mentorship": False
            },
            {"offer_id":30, "helper_id":30, "category": "repairs",
            "title": "Fridge & appliance repair",
            "mentorship": False
            },
            {"offer_id":31, "helper_id":31, "category": "charging",
            "title": "Powerbank rental, R30/hr",
            "mentorship": False
            },
            {"offer_id":32, "helper_id":32, "category": "charging",
            "title": "Charge at my shop, R15/hr",
            "mentorship": False
            },
            {"offer_id":33, "helper_id":33, "category": "charging",
            "title": "Fast Charging, 30min = R15 (charge during loadshedding)",
            "mentorship": False
            },
            {"offer_id":34, "helper_id":34, "category": "sewing",
            "title": "Alterations, from R30",
            "mentorship": False
                        },
            {"offer_id":35, "helper_id":35, "category": "sewing",
            "title": "custom designs & sewing",
            "mentorship": False
            },
            {"offer_id":36, "helper_id":36, "category": "sewing",
            "title": "Hemming & zips",
            "mentorship": False
            },
            {"offer_id":37, "helper_id":37, "category": "rides",
            "title": "Clinic drop-off & back",
            "mentorship": False
            },
            
        ]
        self.free_offers= [
            {"offer_id":38, "helper_id":38, "category": "clothes",
                         "title": "giving away size 30 men's gray pants, still in good shape",
                         "mentorship": False
                        },
                        {"offer_id":39, "helper_id":39, "category": "clothes",
                        "title": "3 dresses, size M, all worn once",
                        "mentorship": False
                                    },
                        {"offer_id":40, "helper_id":40, "category": "clothes",
                        "title": "tekkies, size 6, ladies, almost new",
                        "mentorship": False
                                    },
                        {"offer_id":41, "helper_id":41, "category": "clothes",
                        "title": "Winter jacket, men's large, warm & clean",
                        "mentorship": False
                                    },
                        {"offer_id":42, "helper_id":42, "category": "clothes",
                        "title": "a few jeans, ladies, size 32, good condition",
                        "mentorship": False
                                    },
                        {"offer_id":43, "helper_id":43, "category": "food",
                        "title": " 2kg rice, unopened",
                        "mentorship": False
                                                },
                        {"offer_id":44, "helper_id":44, "category": "food",
                        "title": "10kg unopened maize meal for someone who needs it",
                        "mentorship": False
                                                },
                        {"offer_id":45, "helper_id":45, "category": "food",
                        "title": "tinned pilchards, 3 cans",
                        "mentorship": False
                                                },
                        {"offer_id":46, "helper_id":46, "category": "toiletries",
                        "title": "sanitary pads, 2 packs, still sealed",
                        "mentorship": False
                                                },
                        {"offer_id":47, "helper_id":47, "category": "toiletries",
                        "title": "soap, lotion, roll-on, for anyone in need",
                        "mentorship": False
                                                },
                        {"offer_id":48, "helper_id":48, "category": "toiletries",
                        "title": "toiletries pack",
                        "mentorship": False
                                                },
                        {"offer_id":49, "helper_id":49, "category": "toiletries",
                        "title": "pack of pads, unopened",
                        "mentorship": False
                                                },
                        {"offer_id":50, "helper_id":50, "category": "school",
                        "title": "2 quire notebooks",
                        "mentorship": False
                                                },
                        {"offer_id":51, "helper_id":51, "category": "school",
                        "title": "pens, pencils, books, crayons (all new)",
                        "mentorship": False
                                                },
                        {"offer_id":52, "helper_id":52, "category": "school",
                        "title": "girls' school shoes, size 5, still in good shape",
                        "mentorship": False
                                                },
                        {"offer_id":53, "helper_id":53, "category": "school",
                        "title": "school bag (new)",
                        "mentorship": False
                                                },
                        {"offer_id":54, "helper_id":54, "category": "appliances",
                        "title": "Fridge, good condition",
                        "mentorship": False
                                                },
                        {"offer_id":55, "helper_id":55, "category": "appliances",
                        "title": "microwave, 20L, works fine, just replacing it",
                        "mentorship": False
                                                },
                        {"offer_id":56, "helper_id":56, "category": "appliances",
                        "title": "kettle & iron",
                        "mentorship": False
                                                },
                        {"offer_id":57, "helper_id":57, "category": "furniture",
                        "title": "3 seater couch, good condition",
                        "mentorship": False
                                                },
                        {"offer_id":58, "helper_id":58, "category": "furniture",
                        "title": "wardrobe, 2 door",
                        "mentorship": False
                                                },
                        {"offer_id":59, "helper_id":59, "category": "electronics",
                        "title": "Samsung A05, working, no cracks",
                        "mentorship": False
                                                },
                        {"offer_id":60, "helper_id":60, "category": "electronics",
                        "title": "32 inch TV, working fine",
                        "mentorship": False
                                                },
                        {"offer_id":61, "helper_id":61, "category": "kids",
                        "title": "nappies, small pack, unopened",
                        "mentorship": False
                                                },
                        {"offer_id":62, "helper_id":62, "category": "kids",
                        "title": "baby formula, unopened, 1 tin",
                        "mentorship": False
                                                },
                        {"offer_id":63, "helper_id":63, "category": "tutoring",
                        "title": "Free tutoring, Gr8-9 Maths",
                        "mentorship": True
                                                },
                        
        ]
        self.new_offers= []


    def add_paid_offer (self, content, category, mentorship):

        new_id= 1
        for o in self.paid_offers:
            if o["offer_id"] >=new_id:
                new_id= o["offer_id"]+1
                
        cat= category.lower()
        
        if "hair" in cat:
            cat= "hair"
        if "baked" in cat:
            cat= "baked"
        if "tools" in cat:
            cat = "tools"
        if "rides" in cat:
            cat = "rides"
        if "charging" in cat:
            cat = "charging"
        if "sewing" in cat:
            cat= "sewing"
            

        new_offer= {
            "offer_id": new_id,
            "helper_id":65,
            "category": cat,
            "title": content.strip(),
            "mentorship": mentorship,
        }
        self.paid_offers.append(new_offer)

        return new_offer

    def add_free_offer(self, content, category, mentorship):
        new_id= 1
        for o in self.paid_offers:
            if o["offer_id"] >=new_id:
                new_id= o["offer_id"]+1

        cat= category.lower()

        if "food" in cat:
            cat= "food"
        if "school" in cat: 
            cat = "school"
        if "kids" in cat:
            cat = "kids"

        new_offer= {
            "offer_id": new_id,
            "helper_id":65,
            "category": cat,
            "title": content.strip(),
            "mentorship": mentorship,
            }
        self.free_offers.append(new_offer)
         
        return new_offer
    def get_paid_offers(self, category):
        result= []
        for o in self.paid_offers:
            if o["category"]== category:
                result.append(o)
        
        return result

    def get_free_offers(self, category):
            result= []
            for o in self.free_offers:
                if o["category"]== category:
                    result.append(o)
            
            return result

    def delete_paid_offer(self, offer_id):
        for o in self.paid_offers:
            if o["offer_id"] == offer_id and o["helper_id"] ==65:
                self.paid_offers.remove(o)
                return True
        return False

    def delete_free_offer(self, offer_id):
        for o in self.free_offers:
            if o["offer_id"] == offer_id and o["helper_id"] ==65:
                self.free_offers.remove(o)
                return True
        return False


    def get_rating(self, helper_id):
        ratings= self.users[helper_id].get("ratings", [])
        if not ratings:
            return 0,0
        return sum(ratings)/len(ratings), len(ratings)

    def get_reviews(self, helper_id):
        result = []
        for r in self.reviews:
            if r["helper_id"] == helper_id:
                result.append(r)

        result.reverse()  # newest first
        return result

    def add_review(self, helper_id, stars, comment):
        self.users[helper_id].setdefault("ratings", []).append(stars)
        self.reviews.append({
            "helper_id": helper_id,
            "reviewer_id": 65,
            "stars": stars,
            "comment": comment.strip()
        })

    def has_reviewed(self, helper_id):
        print("checking", helper_id)
        for r in self.reviews:
            if r["helper_id"]== helper_id and r["reviewer_id"] == 65:
                return True
        return False

    def add_report(self, helper_id, reason):
        self.reports.append({
            "helper_id": helper_id,
            "reporter_id": 65,
            "reason": reason
        })