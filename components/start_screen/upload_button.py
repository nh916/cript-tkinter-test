# python package
import tkinter

# my modules
from defaults import default_font, default_font_size


# upload button
def button(root):
    upload_button = tkinter.Button(root, text="Upload Excel File", fg="white", bg="green")
    upload_button.grid(row=6, column=0)
