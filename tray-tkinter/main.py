import customtkinter
import pystray
from PIL import Image, ImageTk

class Window(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.geometry("350x275")
        self.title("CTk Text")
        self.protocol('WM_DELETE_WINDOW', self.hide_window)

    def quit_window(self, icon, item):
        self.icon.stop()
        self.destroy()

    def show_window(self, icon, item):
        self.icon.stop()
        self.after(0, self.deiconify())

    def hide_window(self):
        self.withdraw()
        self.image = Image.open("favicon.ico")
        self.menu=(pystray.MenuItem('Quit', self.quit_window), pystray.MenuItem('Show', self.show_window))
        self.icon = pystray.Icon("name", self.image, "My system tray icon", self.menu)
        self.icon.run()

window = Window()
window.mainloop()
