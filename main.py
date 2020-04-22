import attend
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.theming import ThemeManager
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel

class Login(BoxLayout):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    update = ObjectProperty(None)

    def update_text(self):
        result = attend.get_attendace(self.username.text, self.password.text) 
        self.update.text = result

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Blue"
        self.theme_cls.theme_style = "Dark"

        return Login()

if __name__ == "__main__":
    MainApp().run()