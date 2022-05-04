from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("design.kv")


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
        pass


class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        print(uname, pword)
        pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
