import json
import os
from datetime import datetime
from manager.product import Product

PRODUCTS_FILE = "data/products.json"
SALES_FILE = "data/sales.json"
EXPENSES_FILE = "data/expenses.json"

class Storage:
    def __init__(self):
        self.products = self.load_products()
        self.sales = self.load_sales()
        self.expenses = self.load_expenses()

    # === PRODUCTS ===
    def load_products(self):
        if os.path.exists(PRODUCTS_FILE):
            with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    return [Product(**prod) for prod in data]
                except json.JSONDecodeError:
                    return []  # bo'sh yoki noto'g'ri format
        return []

    def save_products(self):
        with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
            json.dump([vars(p) for p in self.products], f, indent=4, ensure_ascii=False)

    def add_product(self, product: Product):
        self.products.append(product)
        self.save_products()

    def delete_product(self, name: str):
        self.products = [m for m in self.products if m.name != name]
        self.save_products()

    def edit_product(self, eski_nom, yangi_nom=None, yangi_narx=None, yangi_soni=None):
        for product in self.products:
            if product.name == eski_nom:
                product.edit_product(yangi_nom, yangi_narx, yangi_soni)
                self.save_products()
                return True
        return False

    def list_products(self):
        if not self.products:
            print("📭 Hozircha mahsulot yo‘q.")
            return []
        for product in self.products:
            print(product)
        return self.products

    # === SALES ===
    def load_sales(self):
        if os.path.exists(SALES_FILE):
            with open(SALES_FILE, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def save_sales(self):
        with open(SALES_FILE, "w", encoding="utf-8") as f:
            json.dump(self.sales, f, indent=4, ensure_ascii=False)

    def record_sale(self, name, qty, unit_price, total):
        sale = {
            "name": name,
            "qty": qty,
            "unit_price": unit_price,
            "total": total,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.sales.append(sale)
        self.save_sales()

    # === EXPENSES ===
    def load_expenses(self):
        if os.path.exists(EXPENSES_FILE):
            with open(EXPENSES_FILE, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def save_expenses(self):
        with open(EXPENSES_FILE, "w", encoding="utf-8") as f:
            json.dump(self.expenses, f, indent=4, ensure_ascii=False)

    def record_expense(self, name, amount):
        expense = {
            "name": name,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.expenses.append(expense)
        self.save_expenses()

    # === SAVE ALL (optional helper) ===
    def save(self):
        """Barcha ma’lumotlarni saqlash"""
        self.save_products()
        self.save_sales()
        self.save_expenses()
