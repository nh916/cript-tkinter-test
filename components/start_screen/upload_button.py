# python package
import tkinter


# my modules


def upload_to_cript():
    print("uploading to cript :)")


# upload button
def upload_button(root):
    upload_button_tk = tkinter.Button(root, text="Upload Excel File", fg="white", bg="green", command=upload_to_cript)

    upload_button_tk.grid(row=6, column=0)
