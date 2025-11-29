class Solution:
    def findEquilibrium(self, arr):
        total=sum(arr)
        left=0
        for i,x in enumerate(arr):
            total-=x
            if left==total:
                return i
            left+=x
        return -1
