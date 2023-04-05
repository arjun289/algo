import unittest
import reverse_words_str


class TestReverseWords(unittest.TestCase):
    def test_str1(self):
        self.assertEqual("Python love We", 
                         reverse_words_str.reverse_words("We love Python"))
    
    def test_str2(self):
        self.assertEqual("be to not or be To", 
                         reverse_words_str.reverse_words("To be or not to be"))

    def test_str3(self):
        self.assertEqual("amazing are You", 
                         reverse_words_str.reverse_words("You are amazing"))
 
    def test_str4(self):
        self.assertEqual("World Hello",
                         reverse_words_str.reverse_words("Hello World"))

    def test_str5(self):
        self.assertEqual("Hey", reverse_words_str.reverse_words("Hey"))


if __name__ == '__main__':
    unittest.main()
