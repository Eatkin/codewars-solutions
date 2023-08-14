# https://www.codewars.com/kata/5813d19765d81c592200001a
# 2023-08-02T07:16:27.251+0000
def dont_give_me_five(start,end):
    return len([i for i in range(start, end + 1) if not "5" in str(i)])