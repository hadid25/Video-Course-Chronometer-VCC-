import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Video Course Chronometer")
        self.minsize(400,400)



if __name__ == "__main__":
    app = App()
    app.mainloop()

    