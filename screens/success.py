# python package
import tkinter

# my modules


class SuccessScreen:
    def __init__(self, root):
        # main window (root) and loading frame
        self.root = root
        self.frame = tkinter.Frame(root, background="red", height=700, width=700)

    def get_success_screen(self):
        return self.frame
