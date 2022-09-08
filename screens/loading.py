# python package
import tkinter

# my modules
from defaults import default_font, default_font_size


class LoadingScreen:
    def __init__(self, root):
        self.app_window = root

        self.root = root.root

        self.frame = tkinter.Frame(self.root, background="red", height=700, width=700)

        # variables needed for loading frame
        self.cancel_button = None

    # TODO these need _component or something to tell them apart
    def loading_bar(self):
        # show loading bar and picture
        pass

    def _cancel_upload_button_handler(self):
        # stop the uploading program
        pass

    def cancel_upload_button(self):
        self.cancel_button = tkinter.Button(self.frame, text="Cancel Upload")
        self.cancel_button.grid(row=1, column=1)

    def get_loading_screen(self):
        self.cancel_upload_button()
        return self.frame
