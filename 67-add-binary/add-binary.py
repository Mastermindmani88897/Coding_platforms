def bin_to_int(a,b):
    su=0
    n = int(a,2)
    s = int(b,2)
    su = n+s
    su = bin(su)
    return su[2:]

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin_to_int(a,b))