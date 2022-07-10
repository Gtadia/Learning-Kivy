from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class BoxLayoutExample(BoxLayout): # In the kivy file, we made "BoxLayoutExample" the main interface, which is why it takes up the entire window
        """   
        def __init__(self, **kwargs): # We don't use this but this is for the internal working for kivy
        super().__init__(**kwargs) # This is also for the intenral working for kivy
        # How to create and add widets in the python code (you can basically do the same thing on the .kv file)
        b1=Button(text="A")
        b2=Button(text="B")
        b3=Button(text="C")
        
        self.add_widget(b2)
        self.add_widget(b3)
        self.add_widget(b1) # The order of the button is important
        # The box layout will stack the elements horizontally by default
        self.orientation = "vertical" # But you can change the orientation to be vertical like this
        """
        pass # The same thing is going to be recreated in the .kv file

class MainWidget(Widget):
    pass


class FirstKivyApp(App):
    pass

if __name__ == "__main__":
    FirstKivyApp().run()