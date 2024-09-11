from kivy.app import App
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout


Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '400')


class ETStreamDeckApp(App):

    def build(self):

        FL = FloatLayout(size=(700, 500))

        return FL


if __name__ == "__main__":

    ETStreamDeckApp().run()

