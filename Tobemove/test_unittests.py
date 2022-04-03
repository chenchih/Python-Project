import unittest
class Test_test(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(4,4)
    def test_decrement(self):
        self.assertEqual(4,4)

if __name__ =='__main__':
    unittest.main()