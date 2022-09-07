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
host.ask_for_host(root)
api_token.ask_for_api_token(root)
project_name.ask_for_project_name(root)
collection_name.ask_for_collection_name(root)
path_to_excel.ask_for_excel_path(root)
data_privacy.ask_for_data_privacy_option(root)
upload_button.button(root)

# start program
root.mainloop()
