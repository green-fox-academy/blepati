class SumOfNums(object):
    def sum(self, list_of_nums):
        out = 0
        if type(list_of_nums) != list: #checks if list_of_nums is a list
            return 0
        for number in list_of_nums:
            out += number
        return out
