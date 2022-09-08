# python package
import tkinter

# my modules


class ErrorScreen:
    def __init__(self, root):
        self.app_window = root

        self.root = root.root

        self.frame = tkinter.Frame(self.root, background="red", height=700, width=700)

    def get_error_screen(self):
        self.get_error_screen()
        return self.frame
