import tkinter as tk
from tkinter import ttk, messagebox
from .Manage import ManageSell
from datetime import datetime

MANAGE = ManageSell()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.thai = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
        self.price = []
        self.products = []

        # Configure rows and columns to resize with the window
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        label = tk.Label(self, text="Home Page", font=("Arial", 18))
        label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.entry_text = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_text, font=("Arial", 12))
        self.entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.entry.focus()
        self.entry_text.trace_add("write", self.print_hello)

        clear_button = tk.Button(self, text="Clear", command=self.clear_labels, font=("Arial", 12))
        clear_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.tree = ttk.Treeview(self, columns=("Product Name", "Price", "Barcode"), show="headings")
        self.tree.heading("Product Name", text="Product Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Barcode", text="Barcode")
        self.tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    def print_hello(self, *args):
        text = self.entry_text.get()
        if text in self.thai:
            messagebox.showerror("ERROR", "กรุณาตรวจสอบภาษาของท่าน")
            self.entry.delete(0, tk.END)
        else:
            x = MANAGE.search_product(barcode=text)
            if x:
                for item in x:
                    self.tree.insert("", "end", values=(item[1], f"{item[2]} BDT", item[4]))
                    self.price.append(int(item[2]))
                self.products.append(x[0])
                self.entry.delete(0, tk.END)

    def clear_labels(self, event=None):
        # MANAGE.insert_sales(self.products)
        print(datetime.now())
        messagebox.showinfo("Total", f"Total Price: {sum(self.price)} BDT")
        self.tree.delete(*self.tree.get_children())
        self.price = []
        self.products = []
