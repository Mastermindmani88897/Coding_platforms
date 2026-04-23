class Solution:
    def canSplit(self, arr):
        total = sum(arr)
        
        if total % 2 != 0:
            return False
        
        target = total // 2
        curr = 0
        
        for x in arr:
            curr += x
            if curr == target:
                return True
        
        return False