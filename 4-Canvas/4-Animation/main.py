from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Ellipse, Line, Rectangle
from kivy.metrics import dp
from kivy.uix.widget import Widget

from kivy.properties import Clock # This import is used for the Clock.schedule thing... (REMEMBER: It's kivy.PROPERTIES not kivy.CLOCK)



class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        with self.canvas:
            """
            self.center doesn't actually center ellipse because in the __init__ function, we don't 
            have the size of the window already defined (It's too early in the initialization of 
            the window of the graphic

            So, the default size is actually (100, 100) pixels


            ALSO, the center of the ellipse is actually the lower left corner of the ellipse
            """
            # Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
            """Unlike the .kv file, self.center, self.width, self.rect.pos, etc. are not going to update automatically (It's just a line of code)"""

            # We can make the widgets an instance variable inside of the __init__ function (We need the init function to declare and initialize our widgets/classes)
            # Then we can use that instanee variable in a function OUTSIDE of the __init__ function
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))

            """
            If we want to move the ball, we're going to need something that calls a function regularly
            in a certain time interval.
                This is achieved with:
                Clock.schedule_interval()
            """
            Clock.schedule_interval(self.update, 1/60) # (function to execute, the time interval (in seconds) that this function runs)
            # 1/60  =  60 fps



    def on_size(self, *args):
        """If we create another function outside of the __init__ function, which only runs once, we can have a function that automatically updates when something (such as self.width) changes"""
        # print("on size:", str(self.width), ",", str(self.height))  # in other words, as soon as the width and height changes, this function executes
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)

        
    def update(self, dt): # (self, delta time/time interval)
        print("update")
        x, y = self.ball.pos
        self.ball.pos = (x + 1, y)

    
"""EXERCISE"""
class CanvasExample5Exercise(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)

        self.velocity_x = dp(3) # The velocity/speed of the ball (in the x axis) 
        self.velocity_y = dp(3) # The velocity/speed of the ball (in the y axis)

        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
            Clock.schedule_interval(self.update, 1/60)
    
    
    
    def on_size(self, *args):
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)
        



    def update(self, dt):
        x, y = self.ball.pos
        w, h = self.ball.size
        window_w, window_h = self.size # I can either split the size of the window to their respect width and height or just use self.width and self.height

        x += self.velocity_x
        y += self.velocity_y


        if (y <= 0) or (y + h >= window_h):
            self.velocity_y = - self.velocity_y

        if (x <= 0) or (x + w >= self.width):
            self.velocity_x = - self.velocity_x

        

        self.ball.pos = (x, y)
"""EXERCISE"""
"""
    - When the ball touches the top/bottom borders, then we are going to invert velocity_y
    - When the ball touches the left/right borders, then we are going to invert velocity_x
    - If it thouches the corners, we are going to invert both x and y velocities (basically automatically added)
"""
    


class FirstKivyApp(App):
    pass

if __name__ == "__main__":
    FirstKivyApp().run()
