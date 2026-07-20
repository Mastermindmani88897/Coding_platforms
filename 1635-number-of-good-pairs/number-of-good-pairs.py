class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l=Counter(nums)
        s=0
        for key,val in l.items():
            if val>=2:
                s+=(val-1)*val//2
        return s
      
                
