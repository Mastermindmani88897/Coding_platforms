class Solution:
    def getAlternates(self, arr):
        # Code Here
        li=[]
        for i in range(0,len(arr),2):
            li.append(arr[i])
        return li 