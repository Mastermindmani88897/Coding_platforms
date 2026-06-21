class Solution:
    def chooseSwap(self, s):
        first = [-1] * 26
        
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
        
        a = b = None
        
        for i, ch in enumerate(s):
            cur = ord(ch) - ord('a')
            
            for c in range(cur):
                if first[c] > i:
                    a = ch
                    b = chr(c + ord('a'))
                    break
            
            if a is not None:
                break
        
        if a is None:
            return s
        
        res = []
        for ch in s:
            if ch == a:
                res.append(b)
            elif ch == b:
                res.append(a)
            else:
                res.append(ch)
        
        return "".join(res)