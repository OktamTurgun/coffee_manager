import unittest
from manager.storage import Storage
from manager.product import Product

class TestSales(unittest.TestCase):
    def setUp(self):
        # Har bir testdan oldin toza Storage yaratamiz
        self.storage = Storage()
        self.storage.sales = []  # mavjud sotuvlarni tozalash
        self.product = Product(name="Coffee", price=30000, quantity=10)

    def test_record_sale(self):
        # Mahsulotni sotish
        qty_sold = 2
        unit_price = self.product.price
        total = qty_sold * unit_price

        self.storage.record_sale(self.product.name, qty_sold, unit_price, total)

        # Sotuvlar ro'yxatini tekshirish
        self.assertEqual(len(self.storage.sales), 1)
        sale = self.storage.sales[0]
        self.assertEqual(sale["name"], "Coffee")
        self.assertEqual(sale["qty"], qty_sold)
        self.assertEqual(sale["unit_price"], unit_price)
        self.assertEqual(sale["total"], total)
        self.assertIn("date", sale)  # sana mavjudligini tekshirish

if __name__ == "__main__":
    unittest.main()
