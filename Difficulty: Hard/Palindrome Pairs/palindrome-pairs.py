class Solution:
    def palindromePair(self, arr):
        
        def is_palindrome(s):
            return s == s[::-1]
        
        mp = {}
        
        for i, word in enumerate(arr):
            mp[word] = i
        
        for i, word in enumerate(arr):
            n = len(word)
            
            for j in range(n + 1):
                left = word[:j]
                right = word[j:]
                
                if is_palindrome(left):
                    rev = right[::-1]
                    
                    if rev in mp and mp[rev] != i:
                        return True
                
                if j != n and is_palindrome(right):
                    rev = left[::-1]
                    
                    if rev in mp and mp[rev] != i:
                        return True
        
        return False