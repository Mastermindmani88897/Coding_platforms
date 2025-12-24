class Solution:
    def countLessEqual(self, arr, x):
        #code here
        c=0
        for i in range(len(arr)):
            if arr[i]<=x:
                c=c+1
        return c
        