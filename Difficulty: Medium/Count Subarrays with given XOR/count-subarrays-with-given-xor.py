class Solution:
    def subarrayXor(self, arr, k):
        from collections import defaultdict
        
        freq = defaultdict(int)
        freq[0] = 1
        
        xor = 0
        count = 0
        
        for num in arr:
            xor ^= num
            count += freq[xor ^ k]
            freq[xor] += 1
        
        return count