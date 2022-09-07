# python package
import tkinter

# my modules
from defaults import default_font, default_font_size


def loading_screen():
    # create window object
    root = tkinter.Tk()

    # setting up tkinter window
    root.geometry("700x700")
    root.title("CRIPT Excel Uploader")

    # test
    host_label = tkinter.Label(root, text="host:", font=(default_font, default_font_size),
                               justify="left")
    host_label.grid(row=0, column=0)

    # input
    host_entry = tkinter.Entry(root, width=50)
    host_entry.grid(row=0, column=1)

    # start program
    root.mainloop()
