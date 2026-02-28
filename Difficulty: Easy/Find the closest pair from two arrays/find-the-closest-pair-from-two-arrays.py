class Solution:
    def findClosestPair(self, arr1, arr2, x):
        i = 0
        j = len(arr2) - 1
        
        best_diff = float('inf')
        best_pair = (0, 0)
        
        while i < len(arr1) and j >= 0:
            s = arr1[i] + arr2[j]
            diff = abs(s - x)
            
            if diff < best_diff:
                best_diff = diff
                best_pair = (arr1[i], arr2[j])
            
            if s > x:
                j -= 1
            else:
                i += 1
        
        return best_pair