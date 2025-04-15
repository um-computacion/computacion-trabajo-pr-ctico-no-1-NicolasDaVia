import unittest
from roman_converter import decimal_a_romano

class TestDecimalARomano(unittest.TestCase):
    def test_I(self):
        self.assertEqual(decimal_a_romano(1), "I")
    def test_II(self):
        self.assertEqual(decimal_a_romano(2), "II")
    def test_III(self):
        self.assertEqual(decimal_a_romano(3), "III")
    def test_IV(self):
        self.assertEqual(decimal_a_romano(4), "IV")
    def test_V(self):
        self.assertEqual(decimal_a_romano(5), "V")
    def test_VI(self):
        self.assertEqual(decimal_a_romano(6), "VI")
    def test_VII(self):
        self.assertEqual(decimal_a_romano(7), "VII")
    def test_VIII(self):
        self.assertEqual(decimal_a_romano(8), "VIII")
    def test_IX(self):
        self.assertEqual(decimal_a_romano(9), "IX")
    def test_X(self):
        self.assertEqual(decimal_a_romano(10), "X")
    def test_xL(self):
        self.assertEqual(decimal_a_romano(40),"XL")
    def test_L(self):
        self.assertEqual(decimal_a_romano(50), "L")
    def test_XC(self):
        self.assertEqual(decimal_a_romano(90), "XC")
    def test_C(self):
        self.assertEqual(decimal_a_romano(100), "C")
    def test_D(self):
        self.assertEqual(decimal_a_romano(500), "D")
    def test_M(self):
        self.assertEqual(decimal_a_romano(1000), "M")
    
    def test_complex_numbers(self):
        self.assertEqual(decimal_a_romano(49), "XLIX")

        self.assertEqual(decimal_a_romano(99), "XCIX")

        self.assertEqual(decimal_a_romano(499), "CDXCIX")

        self.assertEqual(decimal_a_romano(999), "CMXCIX")

        self.assertEqual(decimal_a_romano(3999), "MMMCMXCIX")
    

if __name__ == "__main__":
    unittest.main()
