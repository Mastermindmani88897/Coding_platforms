class Solution:
    def sumFourDivisors(self, nums):
        def isPrime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        total = 0

        for n in nums:
            found = False

            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    j = n // i
                    if i != j and isPrime(i) and isPrime(j):
                        total += 1 + i + j + n
                        found = True
                    break

            if not found:
                r = round(n ** (1/3))
                if r ** 3 == n and isPrime(r):
                    total += 1 + r + r * r + n

        return total
