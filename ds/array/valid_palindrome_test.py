import unittest
import valid_palindrome


class TestValidPalindrome(unittest.TestCase):
    def test_valid_palindrome1(self):
        self.assertTrue(valid_palindrome.valid_palindrome("madame"))

    def test_valid_palindrome2(self):
        self.assertTrue(valid_palindrome.valid_palindrome("dead"))

    def test_valid_palindrome3(self):
        self.assertTrue(valid_palindrome.valid_palindrome("abca"))

    def test_valid_palindrome4(self):
        self.assertFalse(valid_palindrome.valid_palindrome("tebbem"))

    def test_valid_palindrome5(self):
        self.assertFalse(valid_palindrome.valid_palindrome(
            "eeccccbebaeeabebccceea"))

    def test_valid_palindrome6(self):
        self.assertFalse(valid_palindrome.valid_palindrome(
            "ognfjhgbjhzkqhzadmgqbwqsktzqwjexqvzjsopolnmvnymbbzoofzbbmynvmnloposjzvqxejwqztksqwbqgmdazhqkzhjbghjfno"))


if __name__ == '__main__':
    unittest.main()
