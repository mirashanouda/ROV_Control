from kivymd.app import MDApp
from kivy.lang import Builder

class aqavaders_interface(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        kvPath = "aquavaders_interface.kv"
        self.screen = Builder.load_file(kvPath)

    def build(self):
        return self.screen

if __name__ == "__main__":
    aqavaders_interface().run()