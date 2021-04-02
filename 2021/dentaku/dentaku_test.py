import unittest
from dentaku import Dentaku


class DentakuTest(unittest.TestCase):
    def test_add_ok(self):
        dengtaku = Dentaku()    
        self.assertEqual(3, dengtaku.input("1 + 2"))

    def test_add_no(self):
        dengtaku = Dentaku()    
        self.assertNotEqual(2, dengtaku.input("1 + 2"))


if __name__ == '__main__':
    unittest.main()