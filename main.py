from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

Window.size = (360, 740)

KV = '''
MDScreen:
    md_bg_color: 0.05, 0.08, 0.13, 1

    MDBottomNavigation:
        panel_color: 0.07, 0.10, 0.16, 1
        text_color_active: 0.22, 0.74, 0.98, 1

        MDBottomNavigationItem:
            name: "home"
            text: "Home"
            icon: "home"

            MDBoxLayout:
                orientation: "vertical"

                MDTopAppBar:
                    title: "PS Bikers"
                    elevation: 10
                    md_bg_color: 0.07, 0.10, 0.16, 1

                ScrollView:
                    do_scroll_x: False

                    MDBoxLayout:
                        orientation: "vertical"
                        adaptive_height: True
                        spacing: "14dp"
                        padding: "14dp"

                        MDCard:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "220dp"
                            radius: [24, 24, 24, 24]
                            elevation: 8
                            padding: "18dp"
                            md_bg_color: 0.12, 0.17, 0.26, 1

                            MDLabel:
                                text: "Ride smarter with PS Bikers"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                bold: True
                                font_style: "H5"

                            MDLabel:
                                text: "A mobile rider app concept with map, gatherings, emergency alerts, obstacles, and rider visibility."
                                theme_text_color: "Custom"
                                text_color: 0.82, 0.87, 0.93, 1

                            Widget:

                            MDRaisedButton:
                                text: "Open Map"
                                pos_hint: {"center_x": .5}
                                md_bg_color: 0.22, 0.74, 0.98, 1
                                on_release: app.show_message("Opening map screen")

                        MDLabel:
                            text: "Quick Actions"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            bold: True
                            font_style: "H6"
                            size_hint_y: None
                            height: self.texture_size[1]

                        MDGridLayout:
                            cols: 2
                            adaptive_height: True
                            spacing: "12dp"

                            MDCard:
                                orientation: "vertical"
                                size_hint_y: None
                                height: "170dp"
                                radius: [22, 22, 22, 22]
                                elevation: 6
                                padding: "14dp"
                                md_bg_color: 0.10, 0.14, 0.22, 1

                                MDIcon:
                                    icon: "map-marker-radius"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 0.22, 0.74, 0.98, 1
                                    font_size: "38sp"

                                Widget:

                                MDLabel:
                                    text: "Map"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    bold: True

                                MDRaisedButton:
                                    text: "Open"
                                    pos_hint: {"center_x": .5}
                                    on_release: app.show_message("Map opened")

                            MDCard:
                                orientation: "vertical"
                                size_hint_y: None
                                height: "170dp"
                                radius: [22, 22, 22, 22]
                                elevation: 6
                                padding: "14dp"
                                md_bg_color: 0.10, 0.14, 0.22, 1

                                MDIcon:
                                    icon: "bike-fast"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 0.20, 0.82, 0.39, 1
                                    font_size: "38sp"

                                Widget:

                                MDLabel:
                                    text: "Riders"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    bold: True

                                MDRaisedButton:
                                    text: "Show"
                                    pos_hint: {"center_x": .5}
                                    on_release: app.show_message("Nearby riders shown")

                            MDCard:
                                orientation: "vertical"
                                size_hint_y: None
                                height: "170dp"
                                radius: [22, 22, 22, 22]
                                elevation: 6
                                padding: "14dp"
                                md_bg_color: 0.10, 0.14, 0.22, 1

                                MDIcon:
                                    icon: "account-group"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 0.38, 0.64, 0.98, 1
                                    font_size: "38sp"

                                Widget:

                                MDLabel:
                                    text: "Gatherings"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    bold: True

                                MDRaisedButton:
                                    text: "Create"
                                    pos_hint: {"center_x": .5}
                                    on_release: app.show_message("New gathering created")

                            MDCard:
                                orientation: "vertical"
                                size_hint_y: None
                                height: "170dp"
                                radius: [22, 22, 22, 22]
                                elevation: 6
                                padding: "14dp"
                                md_bg_color: 0.10, 0.14, 0.22, 1

                                MDIcon:
                                    icon: "alert"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 0.94, 0.27, 0.27, 1
                                    font_size: "38sp"

                                Widget:

                                MDLabel:
                                    text: "Emergency"
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    bold: True

                                MDRaisedButton:
                                    text: "Send"
                                    md_bg_color: 0.94, 0.27, 0.27, 1
                                    pos_hint: {"center_x": .5}
                                    on_release: app.show_message("Emergency alert sent")

                        MDCard:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "185dp"
                            radius: [24, 24, 24, 24]
                            elevation: 6
                            padding: "16dp"
                            md_bg_color: 0.09, 0.13, 0.21, 1
                            spacing: "8dp"

                            MDLabel:
                                text: "Upcoming Features"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                bold: True
                                font_style: "H6"

                            MDLabel:
                                text: "• Real map integration\\n• Rider accounts\\n• GPS support\\n• Live alerts\\n• Better APK release"
                                theme_text_color: "Custom"
                                text_color: 0.80, 0.85, 0.92, 1

        MDBottomNavigationItem:
            name: "map"
            text: "Map"
            icon: "map"

            MDBoxLayout:
                orientation: "vertical"

                MDTopAppBar:
                    title: "Map"
                    elevation: 10
                    md_bg_color: 0.07, 0.10, 0.16, 1

                ScrollView:
                    do_scroll_x: False

                    MDBoxLayout:
                        orientation: "vertical"
                        adaptive_height: True
                        spacing: "14dp"
                        padding: "14dp"

                        MDCard:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "330dp"
                            radius: [24, 24, 24, 24]
                            elevation: 8
                            padding: "16dp"
                            spacing: "10dp"
                            md_bg_color: 0.12, 0.17, 0.26, 1

                            MDIcon:
                                icon: "map-marker-radius"
                                halign: "center"
                                theme_text_color: "Custom"
                                text_color: 0.22, 0.74, 0.98, 1
                                font_size: "72sp"

                            MDLabel:
                                text: "Map area"
                                halign: "center"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                bold: True
                                font_style: "H6"

                            MDLabel:
                                text: "This screen is ready for real map integration later."
                                halign: "center"
                                theme_text_color: "Custom"
                                text_color: 0.82, 0.87, 0.93, 1

                        MDGridLayout:
                            cols: 2
                            adaptive_height: True
                            spacing: "12dp"

                            MDRaisedButton:
                                text: "Show Riders"
                                md_bg_color: 0.20, 0.82, 0.39, 1
                                on_release: app.show_message("Showing nearby riders")

                            MDRaisedButton:
                                text: "New Gathering"
                                md_bg_color: 0.38, 0.64, 0.98, 1
                                on_release: app.show_message("New gathering created")

                            MDRaisedButton:
                                text: "Emergency"
                                md_bg_color: 0.94, 0.27, 0.27, 1
                                on_release: app.show_message("Emergency alert created")

                            MDRaisedButton:
                                text: "Report Obstacle"
                                md_bg_color: 0.96, 0.65, 0.16, 1
                                on_release: app.show_message("Obstacle reported")

        MDBottomNavigationItem:
            name: "services"
            text: "Services"
            icon: "apps"

            MDBoxLayout:
                orientation: "vertical"

                MDTopAppBar:
                    title: "Services"
                    elevation: 10
                    md_bg_color: 0.07, 0.10, 0.16, 1

                ScrollView:
                    do_scroll_x: False

                    MDList:
                        OneLineIconListItem:
                            text: "Nearby Riders"
                            on_release: app.show_message("Nearby Riders")
                            IconLeftWidget:
                                icon: "bike-fast"

                        OneLineIconListItem:
                            text: "Gatherings"
                            on_release: app.show_message("Gatherings")
                            IconLeftWidget:
                                icon: "account-group"

                        OneLineIconListItem:
                            text: "Emergency"
                            on_release: app.show_message("Emergency")
                            IconLeftWidget:
                                icon: "alert"

                        OneLineIconListItem:
                            text: "Obstacles"
                            on_release: app.show_message("Obstacles")
                            IconLeftWidget:
                                icon: "road-variant"

                        OneLineIconListItem:
                            text: "Support"
                            on_release: app.show_message("Support opened")
                            IconLeftWidget:
                                icon: "lifebuoy"

        MDBottomNavigationItem:
            name: "profile"
            text: "Profile"
            icon: "account"

            MDBoxLayout:
                orientation: "vertical"

                MDTopAppBar:
                    title: "Profile"
                    elevation: 10
                    md_bg_color: 0.07, 0.10, 0.16, 1

                MDBoxLayout:
                    orientation: "vertical"
                    padding: "14dp"
                    spacing: "14dp"

                    MDCard:
                        orientation: "vertical"
                        size_hint_y: None
                        height: "240dp"
                        radius: [24, 24, 24, 24]
                        elevation: 8
                        padding: "18dp"
                        spacing: "10dp"
                        md_bg_color: 0.12, 0.17, 0.26, 1

                        MDIcon:
                            icon: "account-circle"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0.22, 0.74, 0.98, 1
                            font_size: "80sp"

                        MDLabel:
                            text: "Guest Rider"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            bold: True
                            font_style: "H6"

                        MDLabel:
                            text: "Sign in later to sync gatherings, alerts, and rider status."
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0.82, 0.87, 0.93, 1

                    MDRaisedButton:
                        text: "Contact Support"
                        pos_hint: {"center_x": .5}
                        md_bg_color: 0.65, 0.47, 0.95, 1
                        on_release: app.show_message("Support contact opened")
'''


class PSBikersApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def show_message(self, text):
        Snackbar(
            text=text,
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=(self.root.width - dp(20)) / self.root.width
        ).open()


PSBikersApp().run()