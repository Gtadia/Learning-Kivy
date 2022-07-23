from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line # We are importing "Line" so that we can use it for the canvas
from kivy.graphics.context_instructions import Color # We are importing "Color" for the canvas
from kivy.graphics.vertex_instructions import Rectangle # We are importing "Rectangle" for the canvas
from kivy.metrics import dp 


class CanvasExample1(Widget):
    pass
class CanvasExample2(Widget): 
    pass
class CanvasExample3(Widget):
    pass
    
   

# Why do we want to use the canvas in the code it's because we might want to use some python specific thing, such as looping
class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # In order to use "Line", "Ellipse", "Rectangle", "Color" etc. you have to import them first
            Line(points=(100, 100, 400, 500), width=2) # You can also add more properties/attributes (such as width) to a certain element
            Color(0, 1, 0) # RGB
            Line(circle=(400, 200, 80), width=2) # Notice how "circle" is still lowercase in the Python file (because it's an attribute)
            Line(rectangle=(700, 500, 150, 100), width=5) # Notice how "rectangle" is still lowercase in the Python file (because it's an attribute)
        
            # We are saving the Rectangle object/widget so that we can call it to access/change its attributes
            self.rect = Rectangle(pos=(700, 200), size=(150, 200)) # You have to import "Rectagnle" first before you can use this widget


    """
    # Move the Rectangle
        def on_button_click(self): 
            x, y = self.rect.pos # "pos" returns a list of the x and y position and this line of code stores those values in separate variables
            x += dp(10)
            self.rect.pos = (x, y) # This changes the position of the rectangle

            # Here, we are only moving the position in the x axis
            # So you might be tempted to do this...
            # self.rect.pos[0] += 10
                # However, we can't do this because TUPLES ARE IMMUTABLE
    """

    """EXERCISE"""
    def on_button_click(self):
        x, y = self.rect.pos 
        w, h = self.rect.size # width and height of the rectangle 
        increment = dp(10)

        pos_of_right_side = x + w

        if (pos_of_right_side + increment) >= self.width:
            x += self.width - pos_of_right_side # Increments x by however much it needs to increment by to get to the end of the screen
        else:
            x += increment
        
        self.rect.pos = (x, y) 
    """EXERCISE"""

    """
    # Another solution

        x, y = self.rect.pos 
        w, h = self.rect.size
        increment = dp(10)

        pos_of_right_side = x + w

        difference = self.width - pos_of_right_side
        
        if difference < increment: # if the distance between the right side of the rectangle and the leftmost window border is smaller than the increment, them only increment by however much we need to reach (but not exceed) the window. 
            increment = difference
        
        x += inc
        self.rect.pos = (x, y)  
    """

"""
EXERCISE
    Make the rectangle not move past the right move edge of the window
"""

    


class FirstKivyApp(App):
    pass

if __name__ == "__main__":
    FirstKivyApp().run()