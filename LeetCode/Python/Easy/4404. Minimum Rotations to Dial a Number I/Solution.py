class Solution:
    def minRotations(self, s: str) -> int:
        cur = 0
        ans = 0

        for ch in s:
            nxt = int(ch)
            diff = abs(cur - nxt)
            ans += min(diff, 10 - diff)
            cur = nxt

        return ans