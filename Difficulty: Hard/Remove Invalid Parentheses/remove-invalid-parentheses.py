from collections import deque

class Solution:
    def validParenthesis(self, s):
        
        def is_valid(st):
            count = 0
            
            for ch in st:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    
                    if count < 0:
                        return False
            
            return count == 0
        
        visited = set([s])
        q = deque([s])
        res = []
        found = False
        
        while q:
            cur = q.popleft()
            
            if is_valid(cur):
                res.append(cur)
                found = True
            
            if found:
                continue
            
            for i in range(len(cur)):
                if cur[i] not in '()':
                    continue
                
                nxt = cur[:i] + cur[i + 1:]
                
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        
        return sorted(list(set(res)))