import unittest
import three_sum

class Test3Sum(unittest.TestCase):
    def test_posint_has3sum(self):
        self.assertTrue(three_sum.check_3_sum([1,3,6,4,8,20], 31))
    
    def test_posint1_has3sum(self):
        self.assertTrue(three_sum.check_3_sum([3,7,1,2,8,4,5], 20))

    def test_negint_no3sum(self):
        self.assertFalse(three_sum.check_3_sum([1,-1,-1], 2))


if __name__ == '__main__':
    unittest.main()
