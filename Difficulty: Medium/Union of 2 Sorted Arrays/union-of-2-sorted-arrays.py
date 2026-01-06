class Solution:
    def findUnion(self, a, b):
        # code here 
        num=a+b
        num=list(set(num))
        num.sort()
        return num