class Solution:
    def secondHighest(self, s: str) -> int:
        l=[]
        for i in s:
            if i in '1234567890':
                l.append(int(i))
        print(l)
        l=list(set(l))
        l.sort()
        return l[-2] if len(l)>=2 else -1