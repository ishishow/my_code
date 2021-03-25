import unittest
from main import except_three

class SumTest(unittest.TestCase):
    def test_except_three_ok(self):
        self.assertEqual(18,except_three(10))

    def test_except_three_no(self):
        self.assertNotEqual(36,except_three(10))


if __name__ == '__main__':
    unittest.main()