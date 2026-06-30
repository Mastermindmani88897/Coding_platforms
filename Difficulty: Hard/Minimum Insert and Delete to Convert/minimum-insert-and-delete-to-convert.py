from bisect import bisect_left

class Solution:
    def minInsAndDel(self, a, b):
        s = set(b)
        lis = []

        for x in a:
            if x in s:
                i = bisect_left(lis, x)
                if i == len(lis):
                    lis.append(x)
                else:
                    lis[i] = x

        lcs = len(lis)
        return (len(a) - lcs) + (len(b) - lcs)