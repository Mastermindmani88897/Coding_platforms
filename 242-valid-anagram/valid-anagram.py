from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=Counter(s)
        s2=Counter(t)
        if len(s1-s2)==0 and len(s2-s1)==0:
            return True
        return False
