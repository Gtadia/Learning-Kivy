from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget # Basically a generic widget that doesn't have any specific buttons or labels, or anything other functionality (but it does have all the some basic attributes, such as size_hint of (1, 1))

"""
What we are going to cover...
- GridLayout (Different widgets inside the grid are automatically organized into rows and columns)
- Populate the grid with buttons 
"""

"""
Although you might want to set up the position, size, text, and other characteristics 
inside of the .kv file, you actually CAN'T do everything there. This is because .kv files 
are great for specify layouts that's already a known size and a known position.
"""

class GameScreen(Widget):
    pass

class LanguageLearnerApp(App):
    def build(self):
        return GameScreen() # Since we're not passing in pos or size, we know that it's going to use the default pos of (0, 0) and size_hint of (1, 1)


if __name__ == "__main__":
    LanguageLearnerApp().run()