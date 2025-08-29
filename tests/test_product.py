import unittest
from manager.product import Product

class TestProduct(unittest.TestCase):
    def test_edit_product(self):
        p = Product("Mocha", 18000, 5)
        p.edit_product(yangi_nom="Mocha Deluxe", yangi_narx=20000, yangi_soni=7)
        self.assertEqual(p.name, "Mocha Deluxe")
        self.assertEqual(p.price, 20000)
        self.assertEqual(p.quantity, 7)

if __name__ == "__main__":
    unittest.main()
