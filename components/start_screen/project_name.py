# python package
import tkinter

# my modules
from defaults import default_font, default_font_size


# project name
def project_name(root):
    project_name_label = tkinter.Label(root, text="project name:", font=(default_font, default_font_size),
                                       justify="left")
    project_name_label.grid(row=2, column=0)

    # input
    project_entry = tkinter.Entry(root, width=50)
    project_entry.grid(row=2, column=1)
