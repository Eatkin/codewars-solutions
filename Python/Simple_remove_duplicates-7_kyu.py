# https://www.codewars.com/kata/5ba38ba180824a86850000f7
# 2023-08-09T12:15:15.587+0000
def solve(arr):
    filtered = []
    for i in range(len(arr) - 1):
        if arr[i] not in arr[i + 1:]:
            filtered.append(arr[i])
    filtered.append(arr[-1])
    return filtered