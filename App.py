import tkinter as tk
from app_product.Product import Product
from app_home.Home import HomePage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Routing Example")
        self.geometry("800x600")
        self.fullscreen = False

        self.frames = {}
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")
        
        # Make the container expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (HomePage, Product):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")
        self.create_menu()

        # Bind the F11 key to toggle fullscreen
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.exit_fullscreen)
        self.bind('<Control-c>', self.frames["HomePage"].clear_labels)

    def create_menu(self):
        menu = tk.Menu(self)
        menu.add_command(label="Home", command=lambda: self.show_frame("HomePage"))
        menu.add_command(label="About", command=lambda: self.show_frame("Product"))
        self.config(menu=menu)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.attributes("-fullscreen", self.fullscreen)
        return "break"

    def exit_fullscreen(self, event=None):
        self.fullscreen = False
        self.attributes("-fullscreen", False)
        return "break"

if __name__ == "__main__":
    app = App()
    app.mainloop()
