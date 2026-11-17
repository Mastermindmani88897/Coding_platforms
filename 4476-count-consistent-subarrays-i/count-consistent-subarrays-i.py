class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        
        # Check all possible subarrays (start index i, end index j)
        for i in range(n):
            curr_and = nums[i]
            curr_min = nums[i]
            
            for j in range(i, n):
                curr_and &= nums[j]
                curr_min = min(curr_min, nums[j])
                
                # A subarray is consistent if its bitwise AND equals its minimum value
                if curr_and == curr_min:
                    count += 1
                    
        return count