# python package
import tkinter

# my modules
from defaults import default_font, default_font_size


# path to Excel file
def ask_for_excel_path(root):
    path_to_excel = tkinter.Label(root, text="path to Excel file", font=(default_font, default_font_size),
                                  justify="left")
    path_to_excel.grid(row=4, column=0)
