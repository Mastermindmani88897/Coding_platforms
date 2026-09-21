class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            x = num % k
            new = [0] * k

            new[x] += 1

            for r in range(k):
                if dp[r]:
                    new[(r * x) % k] += dp[r]

            for r in range(k):
                ans[r] += new[r]

            dp = new

        return ans