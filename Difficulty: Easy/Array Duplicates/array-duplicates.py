from collections import Counter
class Solution:
    def findDuplicates(self, arr):
        # code here
        li=[]
        li=Counter(arr)
        c=0
        a=[]
        for key,val in li.items():
            if val==2:
                a.append(key)
        return a
        