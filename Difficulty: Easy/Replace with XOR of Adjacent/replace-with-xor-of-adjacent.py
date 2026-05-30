class Solution:
    def replaceElements(self, arr):
        
        n = len(arr)
        original = arr[:]
        
        arr[0] = original[0] ^ original[1]
        
        for i in range(1, n - 1):
            arr[i] = original[i - 1] ^ original[i + 1]
        
        arr[n - 1] = original[n - 2] ^ original[n - 1]
        
        return arr