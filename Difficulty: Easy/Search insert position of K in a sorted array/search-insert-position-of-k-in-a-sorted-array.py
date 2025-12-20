class Solution:
    def searchInsertK(self, arr, k):
        # code here
        c=0
        for i in range(len(arr)):
            if arr[i]<k:
                c=c+1
            else:
                break
        return c
        