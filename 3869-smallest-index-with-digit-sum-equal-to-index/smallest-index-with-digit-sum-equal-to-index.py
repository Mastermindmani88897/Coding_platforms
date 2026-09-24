from typing import List

def fun(i, j):
    j2 = 0
    while j != 0:
        j2 += j % 10
        j = j // 10  
    return j2 == i

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if fun(i, nums[i]):
                return i
        return -1