#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        a1=set(arr1)
        a2=set(arr2)
        a3=set(arr3)
        li=[]
        li=list(a1 & a2 &a3)
        li.sort()
        return li