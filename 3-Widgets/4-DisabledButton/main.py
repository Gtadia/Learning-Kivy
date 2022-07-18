from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class WidgetsExample(GridLayout):
    count = 0
    count_enabled = False
    my_text = StringProperty("Hello! This is from the main Python file")

    
    def on_button_click(self): 
        if self.count_enabled: # Only once the ToggleButton is enabled can the count button actually increment the number counter. 
            self.count += 1
            print("Button Clicked")
            self.my_text = f"You've clicked the button {self.count} times!"


    def on_toggle_button_state(self, randomName): # the "self" here represents the class 
        print("Toggle State: " + randomName.state) # "randomName.state" should return the state of the ToggleButton 
        
        if randomName.state == "normal":
            randomName.text = "OFF" # Since in the .kv file, we returned the entire ToggleButton element, we are able to change virtually everything about it (including the text displayed on the button)
            self.count_enabled = False # In the off state, the counter is not enabled
        else:
            randomName.text = "ON"
            self.count_enabled = True # In the on state, the counter is enabled
    


class FirstKivyApp(App):
    pass

if __name__ == "__main__":
    FirstKivyApp().run()