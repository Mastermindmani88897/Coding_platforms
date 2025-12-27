class Solution:
    def kthSmallest(self, mat, k):
        # code here
        li=[]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                li.append(mat[i][j])
        li.sort()
        return li[k-1]
        