import customtkinter

class Content1(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.content()

    def content(self):
        self.label = customtkinter.CTkLabel(self, text="Frame #1")
        self.label.grid(row=0, column=0, padx=10)

        self.button = customtkinter.CTkButton(self, text="Change to MyFrame #2", command=lambda: app.change_content())
        self.button.grid(row=1, column=0, padx=20, pady=10)

    

class Content2(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.content()

    def content(self):
        self.label = customtkinter.CTkLabel(self, text="Frame #2")
        self.label.grid(row=0, column=0, padx=10)

        self.button = customtkinter.CTkButton(self, text="Change to MyFrame #1", command=lambda: app.change_content())
        self.button.grid(row=1, column=0, padx=20, pady=10)

class App(customtkinter.CTk):
    content = 1

    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=0)  # configure grid system
        self.grid_rowconfigure(1, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.change_content()

    def change_content(self):
        self.content1()
        if self.content == 1:
            self.content = 2
            self.ctk.destroy()
            self.content1()
        else:
            self.content = 1
            self.ctk.destroy()
            self.content2()
        self.ctk.grid(row=0, column=0, padx=20)

    def content1(self):
        self.ctk = Content1(master=self)

    def content2(self):
        self.ctk = Content2(master=self)

app = App()
app.mainloop()