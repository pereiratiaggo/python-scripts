import customtkinter

class MyFrame(customtkinter.CTkFrame):
    content = 1

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.change_content()

    def change_content(self):
        if self.content == 1:
            self.content = 0
            self.content1()
        else:
            self.content = 1
            self.content2()

    def content1(self):
        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self, text="Frame #1")
        self.label.grid(row=0, column=0, padx=10)

        self.button = customtkinter.CTkButton(self, text="Change to MyFrame #2", command=lambda: self.change_content())
        self.button.grid(row=1, column=0, padx=20, pady=10)

    def content2(self):
        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self, text="Frame #2")
        self.label.grid(row=0, column=0, padx=10)

        self.button = customtkinter.CTkButton(self, text="Change to MyFrame #1", command=lambda: self.change_content())
        self.button.grid(row=1, column=0, padx=20, pady=10)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=0)  # configure grid system
        self.grid_rowconfigure(1, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

app = App()
app.mainloop()