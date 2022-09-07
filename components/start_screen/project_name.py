# python package
import tkinter

# my modules
from defaults import default_font, default_font_size


# project name
def ask_for_project_name(root):
    project_name = tkinter.Label(root, text="project name:", font=(default_font, default_font_size),
                                 justify="left")
    project_name.grid(row=2, column=0)
