import tkinter as tk
from tkinter import ttk, messagebox
from .Manage import ManageProduct
from .Edit import EditProduct

MANAGE = ManageProduct()

class Product(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Initialize the entry widgets as None initially
        self.entry_widgets = {}

        # Display product management interface
        self.show_manage()

    def add_product(self):
        try:
            name = self.value_name.get()
            price = float(self.value_price.get())
            cost = float(self.value_cost.get())
            barcode = self.value_barcode.get()

            result = MANAGE.insert_product(name=name, price=price, cost=cost, barcode=barcode)
            if result["status"] == "error":
                messagebox.showerror("ERROR", result["msg"])
            else:
                messagebox.showinfo("SUCCESS", result["msg"])
                self.clear_entries()
                self.update_table()
        except ValueError:
            messagebox.showerror("ERROR", "Please enter valid numeric values for price and cost.")

    def clear_entries(self):
        self.value_name.set("")
        self.value_price.set("")
        self.value_cost.set("")
        self.value_barcode.set("")

    def update_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        data = MANAGE.find_all()
        for item in data:
            self.tree.insert('', 'end', values=item)

    def show_manage(self):
        manage_page = tk.Frame(self)
        manage_page.pack(fill="both", expand=True, padx=10, pady=10)

        self.create_entry_widgets(manage_page)
        self.create_treeview(manage_page)
        self.update_table()

    def create_entry_widgets(self, parent):
        labels = ["Product Name:", "Price:", "Cost:", "Barcode:"]
        vars = [tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()]
        self.value_name, self.value_price, self.value_cost, self.value_barcode = vars

        for i, (label_text, var) in enumerate(zip(labels, vars)):
            tk.Label(parent, text=label_text).grid(row=0, column=i*2, padx=5, pady=5)
            entry = tk.Entry(parent, textvariable=var)
            entry.grid(row=0, column=i*2+1, padx=5, pady=5)
            self.entry_widgets[label_text] = entry  # Store the entry widgets

        tk.Button(parent, text="Add Product", command=self.add_product).grid(row=0, column=8, padx=5, pady=5)

    def create_treeview(self, parent):
        columns = ("ID", "Name", "Price", "Cost", "Barcode")
        self.tree = ttk.Treeview(parent, columns=columns, show="headings")
        self.tree.grid(row=1, column=0, columnspan=9, padx=5, pady=5, sticky="nsew")

        for col in columns:
            self.tree.heading(col, text=col)

        self.tree.bind("<ButtonRelease-1>", self.edit_product)

        parent.grid_rowconfigure(1, weight=1)
        for i in range(9):
            parent.grid_columnconfigure(i, weight=1)

    def edit_product(self, event):
        selected_items = self.tree.selection()
        if selected_items:
            item = selected_items[0]
            values = self.tree.item(item, "values")
            if values:
                barcode_value = values[4]  # Assuming barcode is the fifth value
                edit = EditProduct(master=self, barcode_value=barcode_value, callback=self.update_table)
                edit.show_id_window()
