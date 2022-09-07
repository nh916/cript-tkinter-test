# python package
import tkinter

# my modules
from defaults import default_font, default_font_size


def handle_data_privacy_option(value):
    print("handling data privacy option")


# public/private
def data_privacy_option(root):
    # data privacy label
    public_or_private = tkinter.Label(root, text="Data Privacy",
                                      font=(default_font, default_font_size))
    public_or_private.grid(row=5, column=0)

    # Radiobutton variable set up
    public_private_option = tkinter.StringVar(value="")
    public_private_option.set(None)

    # public option
    public_or_private_radio_button = tkinter.Radiobutton(root,
                                                         text="public",
                                                         variable=public_private_option,
                                                         value="public",
                                                         command=lambda: handle_data_privacy_option(
                                                             public_private_option.get()
                                                         )
                                                         )
    public_or_private_radio_button.grid(row=6, column=1)

    # private option
    public_or_private_radio_button = tkinter.Radiobutton(root,
                                                         text="private",
                                                         variable=public_private_option,
                                                         value="private",
                                                         command=lambda: handle_data_privacy_option(
                                                             public_private_option.get()
                                                         )
                                                         )
    public_or_private_radio_button.grid(row=7, column=1)
