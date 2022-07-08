from kivy.app import App
from kivy.uix.button import Button

"""
Tasks
- Link our custom widget to .kv file
- Use canvas to specify pos and size
- Use self to get current pos and size
- Use root to get parent pos and size
"""

"""
Although you might want to set up the position, size, text, and other characteristics 
inside of the .kv file, you actually CAN'T do everything there. This is because .kv files 
are great for specify layouts that's already a known size and a known position.
"""

class CustomWidget(Button): 
    pass


class LanguageLearnerApp(App):
    def build(self):
        return CustomWidget( 
            text = "Custom Button",
            pos=(100,100),
            size_hint=(0.25,0.25)
        )


if __name__ == "__main__":
    LanguageLearnerApp().run()