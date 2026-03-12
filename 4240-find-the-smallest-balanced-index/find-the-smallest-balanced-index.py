class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        LIMIT = 10**14  # Max possible prefix sum (10^5 * 10^9)
        
        suffix_prod = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            res = suffix_prod[i + 1] * nums[i]
            suffix_prod[i] = res if res <= LIMIT else LIMIT + 1
            
        prefix_sum = 0
        for i in range(n):
            if prefix_sum == suffix_prod[i + 1]:
                return i
            prefix_sum += nums[i]
            if prefix_sum > LIMIT + 1:
                prefix_sum = LIMIT + 1
                
        return -1
