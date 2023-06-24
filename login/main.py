import customtkinter

class App(customtkinter.CTk):
    
    data = {}
    errors = {}
    ctk_form = {}
    ctk_user = {}

    def __init__(self):
        super().__init__()
        self.geometry("400x250")
        self.title("Login")
        
        self.form()

    def form(self):
        print('Form')
        print()
        self.ctk_form['email'] = customtkinter.CTkEntry(self, placeholder_text="E-mail")
        self.ctk_form['email'].grid(padx=10, pady=10)

        self.ctk_form['password'] = customtkinter.CTkEntry(self, placeholder_text="Password", show="*")
        self.ctk_form['password'].grid(padx=10, pady=10)

        self.ctk_form['submit'] = customtkinter.CTkButton(self, text="Login", command=self.submit)
        self.ctk_form['submit'].grid(padx=10, pady=10)
        print()

    def submit(self):
        print('Submit')
        print()
        if self.validate():
            for key, value in self.ctk_form.items():
                if(hasattr(value, 'get') and callable(getattr(value, 'get'))):
                    self.data[key] = value.get()
                if(hasattr(value, 'destroy') and callable(getattr(value, 'destroy'))):
                    value.destroy()
            self.data['token'] = self.data['email'] + "_" + self.data['password']
            self.user()
        else:
            print(self.errors)
        print()
    
    def validate(self):
        print('validate')
        print()

        self.errors = {}
        if(self.ctk_form['email'].get()==""):
            self.errors['email'] = "Empty email field"
            return False
        
        if(self.ctk_form['password'].get()==""):
            self.errors['password'] = "Empty password field"
            return False
       
        return True

    def user(self):
        print('User')
        print()
        self.ctk_user['email'] = customtkinter.CTkLabel(self, text="E-mail: " + self.data['email'])
        self.ctk_user['email'].grid(padx=10, pady=10)

        self.ctk_user['token'] = customtkinter.CTkLabel(self, text="Token: " + self.data['token'])
        self.ctk_user['token'].grid(padx=10, pady=10)

        self.ctk_user['logout'] = customtkinter.CTkButton(self, text="Logout", command=self.logout)
        self.ctk_user['logout'].grid(padx=10, pady=10)
        print()

    def logout(self):
        print('Logout')
        print()
        for key, value in self.ctk_user.items():
                if(hasattr(value, 'get') and callable(getattr(value, 'get'))):
                    self.data[key] = value.get()
                if(hasattr(value, 'destroy') and callable(getattr(value, 'destroy'))):
                    value.destroy()
        self.form()
        print()


app = App()
app.mainloop()