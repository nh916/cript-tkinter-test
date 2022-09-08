# python package
import tkinter

# my modules
from components.start_screen import host, api_token, project_name, collection_name, path_to_excel, data_privacy, \
    upload_button


def create_start_screen(root):
    start_screen = tkinter.Frame(background="green", height=700, width=700)

    # fields
    host.host(start_screen)
    api_token.api_token(start_screen)
    project_name.project_name(start_screen)
    collection_name.collection_name(start_screen)
    path_to_excel.excel_path(start_screen)
    data_privacy.data_privacy_option(start_screen)

    upload_button.upload_button(start_screen)

    return start_screen
