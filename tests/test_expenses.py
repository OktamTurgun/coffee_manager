import unittest
from manager.storage import Storage

class TestExpenses(unittest.TestCase):
    def setUp(self):
        self.storage = Storage()
        self.storage.expenses = []  # 🔹 test uchun bo'sh ro'yxat

    def test_record_expense(self):
        self.storage.record_expense("Coffee Beans", 50000)
        self.assertEqual(len(self.storage.expenses), 1)
        self.assertEqual(self.storage.expenses[0]["name"], "Coffee Beans")
        self.assertEqual(self.storage.expenses[0]["amount"], 50000)

if __name__ == "__main__":
    unittest.main()

