from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty 

class WidgetsExample(GridLayout):
    count = 0
    count_enabled = BooleanProperty(False) 
    my_text = StringProperty("Hello! This is from the main Python file")

    my_text_input_text = StringProperty() # This is for the label to display the text in the text box everytime enter is pressed.

    
    def on_button_click(self): 
        if self.count_enabled:
            self.count += 1
            print("Button Clicked")
            self.my_text = f"You've clicked the button {self.count} times!"


    def on_toggle_button_state(self, randomName): 
        print("Toggle State: " + randomName.state) 
        
        if randomName.state == "normal":
            randomName.text = "OFF" 
            self.count_enabled = False 
        else:
            randomName.text = "ON"
            self.count_enabled = True 
    

    def on_switch_active(self, anotherRandName):
        print("Switch: " + str(anotherRandName.active)) 

    
    def on_slider_value(self, moreRandName):
        print("Slider: " + str(moreRandName.value))


    # Everytime the function runs, we set the variable "my_text_input_text" to the text within teh textbox 
    def on_text_validate(self, evenMoreRandName):
        self.my_text_input_text = evenMoreRandName.text

class FirstKivyApp(App):
    pass

if __name__ == "__main__":
    FirstKivyApp().run()