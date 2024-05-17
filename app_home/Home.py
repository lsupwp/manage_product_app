import tkinter as tk
from tkinter import ttk, messagebox
from .Manage import ManageSell  # Assuming the ManageSell class is in the same package
from datetime import datetime

MANAGE = ManageSell()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.thai = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
        self.total = []
        self.products = []
        self.quantity = {}

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

        self.tree = ttk.Treeview(self, columns=("Product Name", "Price", "Barcode", "Quantity"), show="headings")
        self.tree.heading("Product Name", text="Product Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Barcode", text="Barcode")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    def print_hello(self, *args):
        text = self.entry_text.get()
        if text in self.thai:
            messagebox.showerror("ERROR", "กรุณาตรวจสอบภาษาของท่าน")
            self.entry.delete(0, tk.END)
        else:
            x = MANAGE.search_product(barcode=text)
            if x:
                product = x[0]
                barcode = product[4]
                if barcode in self.quantity:
                    self.total.append(int(product[2]))
                    self.quantity[barcode] += 1
                    for item in self.tree.get_children():
                        if self.tree.item(item, "values")[2] == barcode:
                            current_quantity = int(self.tree.item(item, "values")[3])
                            self.tree.item(item, values=(product[1], f"{product[2]} บาท", barcode, current_quantity + 1))
                else:
                    self.quantity[barcode] = 1
                    self.tree.insert("", "end", values=(product[1], f"{product[2]} บาท", barcode, self.quantity[barcode]))
                    self.total.append(int(product[2]))
                    self.products.append(product)
                self.entry.delete(0, tk.END)

    def clear_labels(self, event=None):
        messagebox.showinfo("Total", f"Total Price: {sum(self.total)} BDT")
        total = float(sum(self.total))
        date = datetime.now()
        print(MANAGE.insert_sales(total_amount=total, sale_time=date))
        self.print_product_details()  # Print product details before clearing
        self.tree.delete(*self.tree.get_children())
        self.total = []
        self.products = []
        self.quantity = {}

    def print_product_details(self):
        for product in self.products:
            product_id = product[0]
            product_name = product[1]
            price = product[2]
            barcode = product[4]
            quantity = self.quantity[barcode]
            # print(f"Product ID: {product_id}, Product Name: {product_name}, Quantity: {quantity}, Price: {price} บาท")
            MANAGE.insert_saleDetails(product_id=product_id, quantity=quantity, price=price)

