class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        st = [str(x) for x in nums]
        l=[]
        s=Counter(l)
        for i in range(len(st)):
            l=list(st[i])
            s.update(l)
        print(s)
        return s[str(digit)]