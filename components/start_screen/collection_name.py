# python package
import tkinter

# my modules
from defaults import default_font, default_font_size


# collection name
def collection_name(root):
    collection_name_label = tkinter.Label(root, text="collection name:", font=(default_font, default_font_size),
                                    justify="left")
    collection_name_label.grid(row=3, column=0)

    # input
    collection_entry = tkinter.Entry(root, width=50)
    collection_entry.grid(row=3, column=1)
