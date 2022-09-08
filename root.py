# python package
import tkinter

from screens.start import StartScreen

# my modules

user_data = {}

# create window object
root = tkinter.Tk()

# setting up tkinter window
root.geometry("700x700")
root.title("CRIPT Excel Uploader")

start_screen = StartScreen(root=root)
start_screen = start_screen.get_start_screen()
start_screen.pack()

# start program
root.mainloop()
