from collections import Counter
class Solution:
    def majorityElement(self, arr):
        s=-1
        c=Counter(arr)
        n=len(arr)
        for k,v in c.items():
            if v>n//2:
                return k
        return -1
