# python package
import tkinter

# my modules
from screens.loading import loading_screen


def upload_to_cript():
    print("uploading to cript :)")
    loading_screen()


# upload button
def upload_button(root):
    upload_button_tk = tkinter.Button(root, text="Upload Excel File", fg="white", bg="green", command=upload_to_cript)

    upload_button_tk.grid(row=6, column=0)
