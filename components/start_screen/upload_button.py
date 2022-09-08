# python package
import tkinter

# my modules
from screens.loading import loading_screen


def upload_to_cript(frame):
    print("uploading to cript :)")
    frame.pack_forget()


# upload button
def upload_button(frame):
    upload_button_tk = tkinter.Button(frame, text="Upload Excel File", fg="white", bg="green",
                                      command=lambda: upload_to_cript(frame))

    upload_button_tk.grid(row=6, column=0)
