import unittest
from sum_work import SumOfNums

class ListSumMethod(unittest.TestCase):
    def test_list(self):
        num = SumOfNums()
        list_of_nums = [7, 8, 10]
        self.assertEqual(num.sum(list_of_nums), 25)

    def test_list_empty(self):
        num = SumOfNums()
        list_of_nums = []
        self.assertEqual(num.sum(list_of_nums), 0)

    def test_list_one_element(self):
        num = SumOfNums()
        list_of_nums = [7]
        self.assertEqual(num.sum(list_of_nums), 7)

    def test_list_none(self):
        num = SumOfNums()
        list_of_nums = None
        self.assertEqual(num.sum(list_of_nums), 0)

if __name__ == '__main__':
    unittest.main()
