class Solution:
    def overlapInt(self, arr):
        n = len(arr)
        
        start = []
        end = []
        
        for s, e in arr:
            start.append(s)
            end.append(e)
        
        start.sort()
        end.sort()
        
        i = j = 0
        current = 0
        max_overlap = 0
        
        while i < n:
            if start[i] <= end[j]:  # inclusive intervals
                current += 1
                max_overlap = max(max_overlap, current)
                i += 1
            else:
                current -= 1
                j += 1
        
        return max_overlap
