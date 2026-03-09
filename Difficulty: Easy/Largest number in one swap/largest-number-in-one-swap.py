class Solution:
    def largestSwap(self, s):
        s=list(s)
        last=[-1]*10
        for i,ch in enumerate(s):
            last[int(ch)]=i
        for i,ch in enumerate(s):
            for d in range(9,int(ch),-1):
                if last[d]>i:
                    s[i],s[last[d]]=s[last[d]],s[i]
                    return "".join(s)
        return "".join(s)