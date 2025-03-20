

from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDTextButton


class MainApp(MDApp):
    def build(self):
        return Builder.load_file("screen1.kv")  

    # def on_start(self):
    #     self.fps_monitor_start()


MainApp().run()