from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
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
        # This is a loop that creates 5 buttons numbered 1 through 5 
        for i in range(0, 5): 
            b = Button(text=str(i+1), size_hint=(0.2, 0.2))
            self.add_widget(b)

        # This is a loop that creates 5 buttons with a fixed size numbered 6 thorugh 10 
        for i in range (5, 10):
            height = dp(100) + i * 10     # Just here to make the height of each element differents
            b2 = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), height)) # These buttons have a fixed size so when we resize the window, it doesn't change the size of the elements but rather reorganizes/restacks the elements
            self.add_widget(b2)
# class GridLayoutExample(GridLayout):
#     pass


class AnchorLayoutExample(AnchorLayout):
    pass


class StackLayoutForScrollLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"  # Changing the orientation within the custom widget class in the Python file
        
        box_size = dp(100)
        for i in range(0, 101): 
            self.add_widget(Button(text=str(i), size_hint=(None, None), size=(box_size, box_size)))

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