# python package
import tkinter

from screens.start import StartScreen
from screens.loading import LoadingScreen


# TODO we might need lifecycle functions like when to destroy and pack the next screen
# TODO navigating from one frame to another is kinda challenging


# create window object
root = tkinter.Tk()

# setting up tkinter window
root.geometry("700x700")
root.title("CRIPT Excel Uploader")

start_screen = StartScreen(root=root)
start_screen = start_screen.get_start_screen()
# start_screen.pack()

# loading screen
loading_screen = LoadingScreen(root=root)
loading_screen = loading_screen.get_loading_screen()
loading_screen.pack()

# start program
root.mainloop()
