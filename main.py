from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')


class MyApp(App):
    def build(self):
        s = Scatter()
        fl = FloatLayout(size=(300, 300))
        s.add_widget(fl)
        fl.add_widget(Button(text='текст',
                             background_color=[.32, .85, .94, 1],
                             background_normal='',
                             size_hint=(.5, .25),
                             pos=(0, 0)))
        return s


if __name__ == "__main__":
    MyApp().run()
