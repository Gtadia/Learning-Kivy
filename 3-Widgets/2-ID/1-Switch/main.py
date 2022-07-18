from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty 

class WidgetsExample(GridLayout):
    count = 0
    count_enabled = BooleanProperty(False) 
    my_text = StringProperty("Hello! This is from the main Python file")

    
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
        print("Switch: " + str(anotherRandName.active)) # "active" is the "state" of switches (REMEMBER: The "active" property is a boolean, which is why we had to convert it to a boolean value first)
        


class FirstKivyApp(App):
    pass

if __name__ == "__main__":
    FirstKivyApp().run()