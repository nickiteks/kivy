from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')


class MyApp(App):
    def build(self):
        return Button(text = 'текст')


if __name__ == "__main__":
    MyApp().run()
