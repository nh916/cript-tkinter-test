# python package
import tkinter


# my modules


# on click, it gets all the information entered into the start screen
# packs it up into {} and returns it for easy uploading
def upload_to_cript(frame):
    print("uploading to cript :)")
    frame.pack_forget()


# upload button
def upload_button(frame):
    upload_button_tk = tkinter.Button(frame, text="Upload Excel File", fg="white", bg="green",
                                      command=lambda: upload_to_cript(frame))

    upload_button_tk.grid(row=6, column=0)
