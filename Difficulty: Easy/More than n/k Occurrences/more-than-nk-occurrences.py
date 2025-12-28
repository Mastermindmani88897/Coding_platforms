from collections import Counter
class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr, k):
        #Your code here
        n=len(arr)
        c=0
        li=Counter(arr)
        for key,val in li.items():
            if val>n/k:
                c=c+1
        return c