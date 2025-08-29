import unittest
from manager.storage import Storage
from manager.product import Product

class TestStorage(unittest.TestCase):
    def setUp(self):
        # Har testdan oldin yangi Storage obyektini yaratamiz
        self.storage = Storage()

    def test_add_product(self):
        p = Product("Espresso", 12000, 5)
        self.storage.add_product(p)
        self.assertIn(p, self.storage.products)

    def test_delete_product(self):
        p = Product("Latte", 15000, 3)
        self.storage.add_product(p)
        self.storage.delete_product("Latte")
        self.assertNotIn(p, self.storage.products)

if __name__ == "__main__":
    unittest.main()
