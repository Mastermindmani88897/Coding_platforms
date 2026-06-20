class Solution:
    def getLastDigit(self, a, b):
        if b == "0":
            return 1
        
        last = int(a[-1])
        
        exp = 0
        for ch in b:
            exp = (exp * 10 + int(ch)) % 4
        
        if exp == 0:
            exp = 4
        
        return pow(last, exp, 10)