from tkinter import *
import customtkinter
from tkinter import filedialog
import time_engine
import table_class

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Video Course Chronometer")
        self.minsize(500,500)

        #Introduction Label
        self.IntroLabel = customtkinter.CTkLabel(master=self, text='Select the folder containing the course')
        self.IntroLabel.pack(padx=5, pady=20)


        #Course Folder Selection Button
        def select_folder_callback(self):
            #Opening dialog box for selecting directory
            self.directory_name = filedialog.askdirectory(
                initialdir="/", title="Select a folder")
            print(self.directory_name)

        self.SelectFolderButton=customtkinter.CTkButton(master=self, text="Select Course Folder", command=lambda: select_folder_callback(self))
        self.SelectFolderButton.pack(padx = 5, pady=10)








        



if __name__ == "__main__":
    app = App()
    app.mainloop()

