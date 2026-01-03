class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        type1 = 6
        type2 = 6

        for _ in range(2, n + 1):
            new_type1 = (2 * type1 + 2 * type2) % MOD
            new_type2 = (2 * type1 + 3 * type2) % MOD
            type1, type2 = new_type1, new_type2

        return (type1 + type2) % MOD
