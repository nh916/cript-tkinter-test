# python package
import tkinter

# my modules
from components.start_screen import host, api_token, project_name, collection_name, path_to_excel, data_privacy, \
    upload_button

from defaults import default_geometry, default_height, default_width

user_data = {}

# create window object
root = tkinter.Tk()

# setting up tkinter window
root.geometry("700x700")
root.title("CRIPT Excel Uploader")

start_screen = tkinter.Frame(background="red", height=700, width=700)

# fields
host.host(start_screen)
api_token.api_token(start_screen)
project_name.project_name(start_screen)
collection_name.collection_name(start_screen)
path_to_excel.excel_path(start_screen)
data_privacy.data_privacy_option(start_screen)

upload_button.upload_button(start_screen)

start_screen.pack()

# start program
root.mainloop()
