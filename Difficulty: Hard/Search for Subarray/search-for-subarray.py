class Solution:
    def search(self, a, b):
        
        n = len(a)
        m = len(b)
        
        lps = [0] * m
        
        j = 0
        i = 1
        
        while i < m:
            if b[i] == b[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        res = []
        
        i = 0
        j = 0
        
        while i < n:
            
            if a[i] == b[j]:
                i += 1
                j += 1
            
            if j == m:
                res.append(i - j)
                j = lps[j - 1]
            
            elif i < n and a[i] != b[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return res