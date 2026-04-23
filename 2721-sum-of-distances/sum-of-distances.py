class Solution:
    def distance(self, nums):
        from collections import defaultdict
        
        mp = defaultdict(list)
        n = len(nums)
        
        for i, v in enumerate(nums):
            mp[v].append(i)
        
        res = [0] * n
        
        for indices in mp.values():
            prefix = [0] * len(indices)
            prefix[0] = indices[0]
            
            for i in range(1, len(indices)):
                prefix[i] = prefix[i - 1] + indices[i]
            
            for i in range(len(indices)):
                idx = indices[i]
                
                left = i * idx - (prefix[i - 1] if i > 0 else 0)
                right = (prefix[-1] - prefix[i]) - (len(indices) - i - 1) * idx
                
                res[idx] = left + right
        
        return res