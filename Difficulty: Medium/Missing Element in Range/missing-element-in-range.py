class Solution:
    def missingRange(self, arr, low, high):
        #code here
        a=set(arr)
        s=[]
        for i in range(low,high+1,1):
            if i not in a:
                s.append(i)
        return s
                