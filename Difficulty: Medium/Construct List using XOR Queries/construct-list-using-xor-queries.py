class Solution:
    def constructList(self, queries):
        xr = 0
        ans = []
        
        for typ, x in reversed(queries):
            if typ == 1:
                xr ^= x
            else:
                ans.append(x ^ xr)
        
        ans.append(xr)   # initial 0 after all XOR operations
        ans.sort()
        
        return ans