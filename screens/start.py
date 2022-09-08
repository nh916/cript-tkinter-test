# python package
import tkinter
from tkinter import filedialog

# my modules
from defaults import default_font, default_font_size


class StartScreen:

    def __init__(self, root):
        # main window (root) and start_screen frame
        self.root = root
        # TODO style this better and change ratios
        self.frame = tkinter.Frame(root, background="green", height=700, width=700)

        # components needed for start screen
        self.host_entry = None
        self.api_token_entry = None
        self.project_entry = None
        self.collection_entry = None
        self.path_to_excel_entry = None
        self.public_private_option = None

        # this is what will be returned and sent to Excel file to use to upload to CRIPT
        self.CRIPT_connection_dict = {}

    def host(self):
        host_label = tkinter.Label(self.frame, text="host:", font=(default_font, default_font_size),
                                   justify="left")
        host_label.grid(row=0, column=0)

        # input
        self.host_entry = tkinter.Entry(self.frame, width=50)
        self.host_entry.grid(row=0, column=1)

    def api_token(self):
        api_token_label = tkinter.Label(self.frame, text="api token:", font=(default_font, default_font_size))
        api_token_label.grid(row=1, column=0)

        # input
        self.api_token_entry = tkinter.Entry(self.frame, width=50, show="*")
        self.api_token_entry.grid(row=1, column=1)

    def project_name(self):
        project_name_label = tkinter.Label(self.frame, text="project name:", font=(default_font, default_font_size),
                                           justify="left")
        project_name_label.grid(row=2, column=0)

        # input
        self.project_entry = tkinter.Entry(self.frame, width=50)
        self.project_entry.grid(row=2, column=1)

    def collection_name(self):
        collection_name_label = tkinter.Label(self.frame, text="collection name:",
                                              font=(default_font, default_font_size),
                                              justify="left")
        collection_name_label.grid(row=3, column=0)

        # input
        self.collection_entry = tkinter.Entry(self.frame, width=50)
        self.collection_entry.grid(row=3, column=1)

    # excel get path from finder and place into text box
    def _excel_path_handler(self, path_to_excel_entry):
        path_to_excel_file = filedialog.askopenfilename(
            initialdir="/",
            title="Please select your Excel",
            filetypes=(
                ("Excel file", "*.xlsx"),
            )
        )

        path_to_excel_entry.insert(0, path_to_excel_file)

    # Excel finder to path
    def excel_path(self):
        path_to_excel = tkinter.Label(self.frame, text="path to Excel file", font=(default_font, default_font_size))
        path_to_excel.grid(row=4, column=0)

        # button opens finder to get Excel file path
        path_to_excel_button = tkinter.Button(self.frame, text="Pick Excel File",
                                              command=lambda: self._excel_path_handler(self.path_to_excel_entry)
                                              )
        path_to_excel_button.grid(row=4, column=1)

        # input box that shows Excel file path
        self.path_to_excel_entry = tkinter.Entry(self.frame, width=50)
        self.path_to_excel_entry.grid(row=4, column=2)

    #  handles what happens when each radio button is picked
    def _data_privacy_option_handler(self, value):
        print("handling data privacy option")

    # radiobutton for public/private
    def data_privacy_option(self):
        # data privacy label
        public_or_private = tkinter.Label(self.frame, text="Data Privacy",
                                          font=(default_font, default_font_size))
        public_or_private.grid(row=5, column=0)

        # Radiobutton variable set up
        self.public_private_option = tkinter.StringVar(value="")
        self.public_private_option.set(None)

        # public option
        public_or_private_radio_button = tkinter.Radiobutton(self.frame,
                                                             text="public",
                                                             variable=self.public_private_option,
                                                             value="public",
                                                             command=lambda: self._data_privacy_option_handler(
                                                                 self.public_private_option.get()
                                                             )
                                                             )
        public_or_private_radio_button.grid(row=6, column=1)

        # private option
        public_or_private_radio_button = tkinter.Radiobutton(self.frame,
                                                             text="private",
                                                             variable=self.public_private_option,
                                                             value="private",
                                                             command=lambda: self._data_privacy_option_handler(
                                                                 self.public_private_option.get()
                                                             )
                                                             )
        public_or_private_radio_button.grid(row=7, column=1)

        # on click, it gets all the information entered into the start screen
        # packs it up into {} and returns it for easy uploading

    # handles what happens when upload button is clicked
    def _upload_button_handler(self):
        # creates a dict from inputs on start screen
        self.CRIPT_connection_dict = {
            "host": self.host_entry.get(),
            "token": self.api_token_entry.get(),
            "project": self.project_entry.get(),
            "collection": self.collection_entry.get(),
            "public": self.public_private_option.get(),
        }

        # TODO once button is clicked hand over dict from GUI to Excel Uploader

        # wipe away the start screen upon hitting "Upload" button
        self.frame.destroy()

    # upload button
    def upload_button(self):
        upload_button_tk = tkinter.Button(self.frame,
                                          text="Upload Excel File",
                                          fg="white",
                                          bg="green",
                                          command=lambda: self._upload_button_handler()
                                          )

        upload_button_tk.grid(row=6, column=0)

    # create and return start screen from all the components
    def get_start_screen(self):
        self.host()
        self.api_token()
        self.project_name()
        self.collection_name()
        self.excel_path()
        self.data_privacy_option()
        self.upload_button()

        return self.frame
