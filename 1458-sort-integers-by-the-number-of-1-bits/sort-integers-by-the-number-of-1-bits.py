from typing import List

def fun(n):
    return bin(n)[2:].count('1')

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (fun(x), x))