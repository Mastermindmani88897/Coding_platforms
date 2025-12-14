class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2**32
        res = ""
        chars = "0123456789abcdef"
        while num > 0:
            res = chars[num % 16] + res
            num //= 16
        return res
