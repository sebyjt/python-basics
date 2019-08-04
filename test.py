import unittest
import cap
class captest(unittest.TestCase):
    def one_word_test(self):
        word='python'
        result=cap.getcap(word)
        print(result)
        self.assertEqual(result,"Python")
    def two_word_test(self):
        word='python rocks'
        result=cap.getcap(word)
        print(result)
        self.assertEqual(result,"Python Rocks")    
if __name__ =='__main__':
    unittest.main()
