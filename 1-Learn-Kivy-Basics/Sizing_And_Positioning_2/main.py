from kivy.app import App
from kivy.uix.button import Button

"""
Tasks
- Create a custom widget
- Pass in a size and position 
- Set a default size and position (right in the constructor or initializer)
"""

class CustomWidget(Button): # A custom widget is created by creating a class (and you can have it inherit from other widgets, such as the "Button" widget from the Kivy library) 
    def __init__(self, **kwargs):
        super(CustomWidget, self).__init__(**kwargs) # This will call the parent/super constructor (from "Button") and will initialize it 
        self.text="Custom Button Widget"
        self.pos=(100, 100)
        self.size_hint=(0.3, 0.3) 


class LanguageLearnerApp(App):
    def build(self):
        return CustomWidget() # Since it inherited from the already provided "Button" widget, it still has all of the "Button" functionality
        # All of the characteristics of the button has been defined within the custom button widget class
        


if __name__ == "__main__":
    LanguageLearnerApp().run()