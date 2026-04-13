class Solution:
    def nextPalindrome(self, num):
        n = len(num)
        res = num[:]
        
        for i in range(n // 2):
            res[n - i - 1] = res[i]
        
        if res > num:
            return res
        
        carry = 1
        mid = n // 2
        
        if n % 2 == 1:
            res[mid] += carry
            carry = res[mid] // 10
            res[mid] %= 10
            i = mid - 1
        else:
            i = mid - 1
        
        j = mid if n % 2 == 0 else mid + 1
        
        while i >= 0:
            res[i] += carry
            carry = res[i] // 10
            res[i] %= 10
            res[j] = res[i]
            i -= 1
            j += 1
        
        if carry:
            res = [1] + [0] * (n - 1) + [1]
        
        return res