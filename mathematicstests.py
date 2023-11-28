import mathematics
import unittest

class Testit(unittest.TestCase):

    def test_add(self):
        self.assertEqual(mathematics.add(5, 4), 9)

    def test_multiply(self):
        self.assertEqual(mathematics.multiply(3, 4), 12)

    def test_power(self):
        self.assertEqual(mathematics.power(2, 8), 256)

if __name__ == '__main__':
    unittest.main()