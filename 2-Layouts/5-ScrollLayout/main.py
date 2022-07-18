from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.metrics import dp # You need to import dp if you want to use it to define the size of elements inside of the custom widget class

"""
Since all of the custom widgets that we make are just fillers, we can basically create the same custom below created below
(the two lines of code that are commented out) inside of the .kv file. 

However, if you're going to add anything OTHER than "pass" inside of the class for the custom widget, then you're going to
need the class/you can't do anything but define attributes inside of the .kv file.
"""
class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"  # Changing the orientation within the custom widget class in the Python file
        
        box_size = dp(100)
        for i in range(0, 101): 
            self.add_widget(Button(text=str(i), size_hint=(None, None), size=(box_size, box_size)))




class FirstKivyApp(App):
    pass

if __name__ == "__main__":
    FirstKivyApp().run()