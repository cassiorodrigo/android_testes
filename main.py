from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.lang.builder import Builder


class Gerenciador(ScreenManager):
    pass


class TelaLogin(Screen):
    pass


class TelaPrincipal(Screen):
    pass


class TesteAndroid(MDApp):

    def on_pause(self):
        pass

    def on_resume(self):
        pass

    def on_stop(self):
        pass

    def build(self):
        sm = Gerenciador()
        sm.add_widget(TelaLogin(name="telalogin"))
        sm.add_widget(TelaPrincipal(name="telaprincipal"))
        build = Builder.load_file("android_ui.kv")
        return build


# if __name__ == "__main__":
teste = TesteAndroid()
teste.run()



