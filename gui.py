# python package
import tkinter

# my modules
# from components.start_screen.host import setup_host
from components.start_screen import host, api_token, project_name, collection_name, path_to_excel, data_privacy, upload_button

# create window object
root = tkinter.Tk()

# setting up tkinter window
root.geometry("700x700")
root.title("CRIPT Excel Uploader")

# fields
host.host(root)
api_token.api_token(root)
project_name.project_name(root)
collection_name.collection_name(root)
path_to_excel.excel_path(root)
data_privacy.data_privacy_option(root)

upload_button.upload_button(root)

# start program
root.mainloop()
