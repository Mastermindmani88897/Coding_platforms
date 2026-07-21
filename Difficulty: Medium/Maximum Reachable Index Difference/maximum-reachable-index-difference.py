class Solution:
    def maxIndexDifference(self, s):
        n = len(s)
        NEG = -1

        best = [NEG] * 26
        ans = -1

        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('a')

            if c == 25:
                far = i
            elif best[c + 1] != NEG:
                far = best[c + 1]
            else:
                far = i

            if far > best[c]:
                best[c] = far

            if c == 0:
                ans = max(ans, far - i)

        return ans