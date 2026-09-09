class Solution:
    def findMax(self, n):
        s = str(n)
        ans = n
        best = sum(map(int, s))

        for i in range(len(s)):
            if s[i] == '0':
                continue

            x = int(s[:i] + str(int(s[i]) - 1) + '9' * (len(s) - i - 1))
            digit_sum = sum(map(int, str(x)))

            if digit_sum > best or (digit_sum == best and x > ans):
                best = digit_sum
                ans = x

        return ans