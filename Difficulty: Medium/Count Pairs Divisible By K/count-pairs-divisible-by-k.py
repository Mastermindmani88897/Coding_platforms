class Solution:
    def countKdivPairs(self, arr, k):
        freq = [0] * k
        ans = 0

        for x in arr:
            rem = x % k
            ans += freq[(k - rem) % k]
            freq[rem] += 1

        return ans