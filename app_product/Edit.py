import tkinter as tk
from .Manage import ManageProduct
from tkinter import messagebox

class EditProduct:
    def __init__(self, master, barcode_value, callback):
        self.master = master
        self.barcode_value = barcode_value
        self.callback = callback
        self.manage_product = ManageProduct()
        
        self.edit_window = tk.Toplevel(master)
        self.edit_window.title("Selected ID")
        self.edit_window.geometry("800x600")
        self.edit_window.resizable(False, False)
        
        # self.show_id_window()

    def edit_func(self):
        try:
            name = self.edit_name_value.get()
            price = float(self.edit_price_value.get())
            cost = float(self.edit_cost_value.get())
            barcode = self.edit_barcode_value.get()
            result = self.manage_product.update_product(name=name, price=price, cost=cost, barcode=barcode)
            if result["status"] == "error":
                messagebox.showerror("ERROR", result["msg"])
            else:
                messagebox.showinfo("SUCCESS", result["msg"])
                self.edit_window.destroy()
                self.callback()
        except ValueError:
            messagebox.showerror("ERROR", "Please enter valid numeric values for price and cost.")
        
    def delete_func(self):
        barcode = self.edit_barcode_value.get()
        result = self.manage_product.delete_product(barcode=barcode)
        if result["status"] == "error":
            messagebox.showerror("ERROR", result["msg"])
        else:
            messagebox.showinfo("SUCCESS", result["msg"])
            self.edit_window.destroy()
            self.callback()

    def show_id_window(self):
        self.edit_frame = tk.Frame(self.edit_window)
        self.edit_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        data = self.manage_product.find_one(barcode=self.barcode_value)
        if not data:
            messagebox.showerror("ERROR", "ไม่มีสินค้านี้")
            return

        product = data[0]
        self.edit_name_value = tk.StringVar(value=product[1])
        self.edit_price_value = tk.StringVar(value=product[2])
        self.edit_cost_value = tk.StringVar(value=product[3])
        self.edit_barcode_value = tk.StringVar(value=product[4])

        self._create_label_entry("ชื่อสินค้า ", self.edit_name_value, 0)
        self._create_label_entry("ราคาสินค้า ", self.edit_price_value, 1)
        self._create_label_entry("ต้นทุนสินค้า ", self.edit_cost_value, 2)
        self._create_label_entry("บาร์โค๊ด ", self.edit_barcode_value, 3)

        tk.Button(self.edit_frame, text="บันทึกข้อมูล", command=self.edit_func).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(self.edit_frame, text="ลบสินค้า", command=self.delete_func).grid(row=4, column=1, padx=5, pady=5)

    def _create_label_entry(self, text, text_var, row):
        tk.Label(self.edit_frame, text=text).grid(row=row, column=0, padx=5, pady=5)
        tk.Entry(self.edit_frame, textvariable=text_var).grid(row=row, column=1, padx=5, pady=5)
