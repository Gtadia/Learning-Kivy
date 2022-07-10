from kivy.app import App
from kivy.uix.button import Button


class LanguageLearnerApp(App):
    def build(self):
        return Button(
            text="Hello World", # Can take in anything (text, image, color, etc.)
            # positions start at (0, 0), which is at the bottom left corner
            pos=(100, 100), # in pixels
            size_hint=(None, None), # size_hint is the percent of the width and height that the child (Button) of the parent (LanguageLearnerApp)'s size (the default is (1, 1), which means the widiget/child/(Button) takes up 100% of the parent width and height)
            # By saying (None, None), we're telling Kivy that we're not going to size the button based on the size of the parent 
            size=(500, 300) # And therefore, only the (size) will adjust the size of the button (adding the size of the button manually)
            )


if __name__ == "__main__":
    LanguageLearnerApp().run()




