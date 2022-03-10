from kivymd.app import MDApp
from kivy.lang import Builder
import subprocess 

class aqavaders_interface(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        kvPath = "aquavaders_interface.kv"
        self.screen = Builder.load_file(kvPath)

    def build(self):
        return self.screen

    def lunch(self, *args):
        #subprocess.run("bash Scripts/joy.sh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #subprocess.run("bash Scripts/joy.sh", shell=True)
        subprocess.run("bash script.sh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == "__main__":
    aqavaders_interface().run()