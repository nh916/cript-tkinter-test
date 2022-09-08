# python package
import tkinter

# my modules
from defaults import default_font, default_font_size


# host
def host(root):
    host_label = tkinter.Label(root, text="host:", font=(default_font, default_font_size),
                               justify="left")
    host_label.grid(row=0, column=0)

    # input
    host_entry = tkinter.Entry(root, width=50)
    host_entry.grid(row=0, column=1)
