class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se=set()
        l=0
        left=0
        for i in range(len(s)):
            while s[i] in se:
                se.remove(s[left])
                left+=1
            se.add(s[i])
            l=max(l,i-left+1)
        return l