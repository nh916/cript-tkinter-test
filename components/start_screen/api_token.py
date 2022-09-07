# python package
import tkinter

# my modules
from defaults import default_font, default_font_size


# api token
def api_token(root):
    api_token_label = tkinter.Label(root, text="api token:", font=(default_font, default_font_size))
    api_token_label.grid(row=1, column=0)

    # input
    api_token_entry = tkinter.Entry(root, width=50, show="*")
    api_token_entry.grid(row=1, column=1)
