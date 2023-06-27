import tkinter
import pystray
from PIL import Image, ImageTk

class Window(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("700x350")
        self.title("System Tray App")
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
