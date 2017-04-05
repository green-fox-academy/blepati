import unittest
from apples_work import Apple


class AppleTest(unittest.TestCase):
    def test_apple_class(self):
        apple = Apple()
        self.assertEquals(apple.get_apples(), "apple")

if __name__ == '__main__':
    unittest.main()
