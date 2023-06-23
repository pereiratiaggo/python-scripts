import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("350x275")
window.title("Login")

def submit():
    print(email, password, checkbox)

text = customtkinter.CTkLabel(window, text="Login")
text.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(window, placeholder_text="E-mail")
email.pack(padx=10, pady=10)

password = customtkinter.CTkEntry(window, placeholder_text="Password", show="*")
password.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(window, text="Remeber Password")
checkbox.pack(padx=10, pady=10)

submit = customtkinter.CTkButton(window, text="Submit", command=submit)
submit.pack(padx=10, pady=10)

print('start')
window.mainloop()
print('end')