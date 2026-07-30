from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        l=Counter(word)
        li=list(l.values())
        li.sort(reverse="True")
        print(li)
        s=0
        for i in range(len(li)):
            if i<=7:
                s+=1
            elif i>7 and i<=15:
                s=s+2
            elif i>15 and i<=23:
                s+=3
            else:
                s+=4

        return s