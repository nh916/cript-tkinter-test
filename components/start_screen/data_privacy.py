# python package
import tkinter

# my modules
from defaults import default_font, default_font_size


# public/private
def ask_for_data_privacy_option(root):
    public_or_private = tkinter.Label(root, text="Data Privacy", font=(default_font, default_font_size))
    public_or_private.grid(row=5, column=0)

    public_option = tkinter.StringVar

    public_or_private_radio_button = tkinter.Radiobutton(root, text="public",
                                                         variable=public_option,
                                                         value="public")
    public_or_private_radio_button.grid(row=6, column=1)

    private_option = tkinter.StringVar
    public_or_private_radio_button = tkinter.Radiobutton(root, text="private",
                                                         variable=private_option,
                                                         value="private")
    public_or_private_radio_button.grid(row=7, column=1)
