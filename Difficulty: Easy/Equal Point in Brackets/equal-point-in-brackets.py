class Solution:
    def findIndex(self, s):
        n = len(s)
        
        total_close = s.count(')')
        open_count = 0
        close_right = total_close
        
        for i in range(n + 1):
            if open_count == close_right:
                return i
            
            if i < n:
                if s[i] == '(':
                    open_count += 1
                else:
                    close_right -= 1
        
        return n