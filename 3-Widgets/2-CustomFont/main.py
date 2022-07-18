from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class WidgetsExample(GridLayout):
    count = 0
    my_text = StringProperty("Hello! This is from the main Python file") # StringProperty has to be imported 
    def on_button_click(self): # This is the function that we're going to pass into "on_press" in the .kv file
        self.count += 1 # everytime the button is clicked, this function runs and increments "count" on every click
        print("Button Clicked")
        self.my_text = f"You've clicked the button {self.count} times!" # This needs to be a "self.my_text" because or else it's going to create a separate local variable called "my_text"

    


class FirstKivyApp(App):
    pass

if __name__ == "__main__":
    FirstKivyApp().run()