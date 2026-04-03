from typing import List
from collections import defaultdict

class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid = n // 2
        
        left = nums[:mid]
        right = nums[mid:]
        
        left_map = defaultdict(int)
        
        for mask in range(1 << len(left)):
            xor_val = 0
            count = 0
            for i in range(len(left)):
                if mask & (1 << i):
                    xor_val ^= left[i]
                    count += 1
            left_map[xor_val] = max(left_map[xor_val], count)
        
        max_keep = -1
        
        for mask in range(1 << len(right)):
            xor_val = 0
            count = 0
            for i in range(len(right)):
                if mask & (1 << i):
                    xor_val ^= right[i]
                    count += 1
            
            need = target ^ xor_val
            if need in left_map:
                max_keep = max(max_keep, count + left_map[need])
        
        if max_keep == -1:
            return -1
        
        return n - max_keep