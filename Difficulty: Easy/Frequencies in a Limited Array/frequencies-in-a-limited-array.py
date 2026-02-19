from collections import Counter
class Solution:
    def frequencyCount(self, arr):
        #  code here
        l=Counter(arr)
        li=[]
        for i in range(1,len(arr)+1,1):
            if i in l:
                li.append(l[i])
            else:
                li.append(0)
        return li
            
