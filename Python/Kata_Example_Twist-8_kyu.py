# https://www.codewars.com/kata/525c1a07bb6dda6944000031
# 2023-07-28T17:21:51.481+0000
class CodewarsFiller:
    def __init__(self):
        self.websites = []

    def get_codewars(self):
        return "codewars"

    def fill_subarray_with_codewars(self):
        subarray = []
        for _ in range(10):
            subarray.append(self.get_codewars())
        return subarray

    def fill_array_with_codewars(self, num_times):
        for _ in range(num_times // 10):
            self.websites.extend(self.fill_subarray_with_codewars())
        remainder = num_times % 10
        for _ in range(remainder):
            self.websites.append(self.get_codewars())


codewars_filler = CodewarsFiller()
codewars_filler.fill_array_with_codewars(1000)
websites = codewars_filler.websites