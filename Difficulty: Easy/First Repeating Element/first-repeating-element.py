from collections import Counter
class Solution:
    def firstRepeated(self,arr):
        # code here 
        l=Counter(arr)
        for i in range(len(arr)):
            if l[arr[i]]>1:
                return i+1
        return -1