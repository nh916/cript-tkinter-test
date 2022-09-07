# python package
import tkinter

# my modules
from defaults import default_font, default_font_size


# collection name
def ask_for_collection_name(root):
    collection_name = tkinter.Label(root, text="collection name:", font=(default_font, default_font_size),
                                    justify="left")
    collection_name.grid(row=3, column=0)
