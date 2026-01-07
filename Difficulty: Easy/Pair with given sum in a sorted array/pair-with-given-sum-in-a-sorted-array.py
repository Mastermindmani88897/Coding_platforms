#User function Template for python3

from collections import Counter
class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        l=Counter(arr)
        s=0
        for x in l:
            y=target-x
            if y in l:
                if x==y:
                    s+=l[x]*(l[x]-1)//2
                elif x<y:
                    s+=l[x]*l[y]
        return  s