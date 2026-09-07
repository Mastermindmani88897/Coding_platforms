class Solution:
    def minCount(self, arr):
        n = len(arr)
        dp = {(-1, 101): 0}

        for x in arr:
            new = dp.copy()

            for (inc, dec), count in dp.items():
                if inc == -1 or x > inc:
                    state = (x, dec)
                    new[state] = max(new.get(state, 0), count + 1)

                if dec == 101 or x < dec:
                    state = (inc, x)
                    new[state] = max(new.get(state, 0), count + 1)

            dp = new

        return n - max(dp.values())