class Product:
    def __init__(self, name: str, price: float, quantity: int, category: str = None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category  # yangi atribut

    def __str__(self):
        cat_info = f" | Kategoriya: {self.category}" if self.category else ""
        return f"{self.name} | Narxi: {self.price:,} so‘m | Soni: {self.quantity} dona{cat_info}"

    def edit_product(self, yangi_nom=None, yangi_narx=None, yangi_soni=None, yangi_category=None):
        if yangi_nom:
            self.name = yangi_nom
        if yangi_narx is not None:
            self.price = yangi_narx
        if yangi_soni is not None:
            self.quantity = yangi_soni
        if yangi_category:
            self.category = yangi_category


