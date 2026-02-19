class Solution:
    def intersectSize(self,a, b):
        # code here
        return len(set(a) & set(b))
