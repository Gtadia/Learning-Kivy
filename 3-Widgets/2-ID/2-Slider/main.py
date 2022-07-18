from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty 

class WidgetsExample(GridLayout):
    count = 0
    count_enabled = BooleanProperty(False) 
    my_text = StringProperty("Hello! This is from the main Python file")

    # slider_value_txt = StringProperty("50") # This will store the value of the slider in order to display it on a label

    
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
        print("Slider: " + str(moreRandName.value)) # "value" is the attribute that stores the value of the position of the slider (It returns a float variable)
        # self.slider_value_txt = str(int(moreRandName.value))



class FirstKivyApp(App):
    pass

if __name__ == "__main__":
    FirstKivyApp().run()