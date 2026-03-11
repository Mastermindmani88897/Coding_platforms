class Solution:
    def bitwiseComplement(self, x: int) -> int:
        if x==0:
            return 1
        return 	x ^ ((1 << x.bit_length()) - 1)