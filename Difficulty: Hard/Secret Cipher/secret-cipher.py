class Solution:
    def compress(self, s):
        n = len(s)

        z = [0] * n
        l = r = 0

        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])

            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1

            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1

            if i % 2 == 0:
                half = i // 2

                if z[half] >= half:
                    dp[i] = min(dp[i], dp[half] + 1)

        ans = []
        i = n

        while i > 0:
            if i % 2 == 0:
                half = i // 2

                if z[half] >= half and dp[i] == dp[half] + 1:
                    ans.append('*')
                    i = half
                    continue

            ans.append(s[i - 1])
            i -= 1

        return ''.join(reversed(ans))