class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        minn=min(len(w1),len(w2))
        maxx=max(len(w1),len(w2))
        li=[]
        for i in range(minn):
            li.append(w1[i])
            li.append(w2[i])
        s=''.join(li)
        if(len(w1)==len(w2)):
            return s
        elif(len(w1)<len(w2)):
            return s+w2[minn:]
        return s+w1[minn:]