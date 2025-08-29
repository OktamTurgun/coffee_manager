import unittest
from manager.category import Category

class TestCategory(unittest.TestCase):
    def test_create_category(self):
        cat = Category("Hot Drinks")
        self.assertEqual(cat.name, "Hot Drinks")

if __name__ == "__main__":
    unittest.main()
