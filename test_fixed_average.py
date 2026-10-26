import unittest
from fixed_average import average

class AverageTests(unittest.TestCase):
    def test_regular_values(self): self.assertEqual(average([4, 8, 12]), 8)
    def test_empty_values(self): self.assertIsNone(average([]))
    def test_single_value(self): self.assertEqual(average([7]), 7)

if __name__ == "__main__": unittest.main()
