# python package
import tkinter

# my modules
from defaults import default_font, default_font_size


# api token
def ask_for_api_token(root):
    api_token = tkinter.Label(root, text="api token:", font=(default_font, default_font_size),
                              justify="left")
    api_token.grid(row=1, column=0)

    api_token_entry = tkinter.Entry(root, width=50, show="*")
    api_token_entry.grid(row=1, column=1)
