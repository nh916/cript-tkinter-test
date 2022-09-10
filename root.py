# python package
import tkinter

from screens.error import ErrorScreen
from screens.loading import LoadingScreen
from screens.start import StartScreen
from screens.success import SuccessScreen


class RootWindow:













    def __init__(self):
        # setting up tkinter window
        self.root = tkinter.Tk()

        self.root.geometry("700x700")
        self.root.title("CRIPT Excel Uploader")

        # screens needed and will be used
        self.start_screen = None
        self.loading_screen = None
        self.error_screen = None
        self.success_screen   =             None



    def start_screen_setup(self):
        self.start_screen = StartScreen(
            root=self
            )
        self.start_screen = self.start_screen.get_start_screen()
        self.start_screen.pack()

    def navigate_from_start_to_loading(self):
        print("navigating from start to loading screen")
        self.start_screen.destroy()
        self.loading_screen_setup()

    def loading_screen_setup(self):
        self.loading_screen = LoadingScreen(root=self)
        self.loading_screen = self.loading_screen.get_loading_screen()
        self.loading_screen.pack()

    def error_screen_setup(self):
        self.error_screen = ErrorScreen(root=self.root)
        self.error_screen = self.error_screen.get_error_screen()
        self.error_screen.pack()

    def success_screen_setup(self):
        self.success_screen = SuccessScreen(root=self.root)
        self.success_screen = self.success_screen.get_success_screen()
        self.success_screen.pack()

    def start_gui(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = RootWindow()
    app.start_screen_setup()

    # this always goes last
    app.root.mainloop()
