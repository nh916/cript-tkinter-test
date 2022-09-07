# python package
import tkinter
from tkinter import filedialog

# my modules
from defaults import default_font, default_font_size


# path to Excel file
def excel_path(root):
    path_to_excel = tkinter.Label(root, text="path to Excel file", font=(default_font, default_font_size))
    path_to_excel.grid(row=4, column=0)
    
    # input
    path_to_excel_entry = tkinter.Entry(root, width=50)
    path_to_excel_entry.grid(row=4, column=1)
