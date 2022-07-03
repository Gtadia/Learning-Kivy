from kivy.app import App  # You have to import the 'App' module before you can use it
from kivy.uix.widget import Widget


"""
Defining the main interface of our program. 
"""
class MainWidget(Widget):
    # This class will inherit from the "Widget" module in the "kivy.uix.widget" library
    pass


class FirstKivyApp(App):
    # This class will inherit from the 'App' class defined in Kivy
    pass


"""
We can write code directly inside the classes but instead, it's recommended that we define the classes here and 
write the code in the ".kv" (FirstKivy.kv) file.
"""
FirstKivyApp().run()