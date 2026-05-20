def isfun(index,A,B):
    c=0
    for i in range(0,index+1):
        for j in range(0,index+1):
            if A[i]==B[j]:
                c=c+1
    return c

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        li=[]
        for i in range(len(A)):
            r=isfun(i,A,B)
            li.append(r)
        return li
        