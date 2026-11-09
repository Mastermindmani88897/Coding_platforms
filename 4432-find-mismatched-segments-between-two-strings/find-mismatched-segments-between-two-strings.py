class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        n = len(s1)
        res = []
        i = 0
        
        while i < n:
            # Find the start of a mismatched segment
            if s1[i] != s2[i]:
                start = i
                # Find the end of the maximal contiguous mismatched segment
                while i < n and s1[i] != s2[i]:
                    i += 1
                end = i
                # Extract substrings corresponding to this segment
                res.append([s1[start:end], s2[start:end]])
            else:
                i += 1
                
        return res