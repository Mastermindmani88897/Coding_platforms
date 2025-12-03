#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a.sort()
        b.sort()
        a1=Counter(a)
        b1=Counter(b)
        c=0
        
        for key,val in b1.items():
            if b1[key]<=a1[key]:
                c=c+1
        if c==len(b1):
            return True
        return False
        
    
