# python package
import tkinter

# my modules


class BaseScreen:
    def __init__(self, root, frame):
        # main window (root) and loading frame
        self.root = root

        self.frame = frame

    def get_screen(self):
        return self.frame
