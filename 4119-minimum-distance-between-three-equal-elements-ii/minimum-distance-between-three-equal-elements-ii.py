from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        ans = float('inf')
        
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            for i in range(len(indices) - 2):
                a, b, c = indices[i], indices[i+1], indices[i+2]
                ans = min(ans, 2 * (c - a))
        
        return ans if ans != float('inf') else -1