class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        li=[]
        s=0
        li.append(s)
        for i in range(len(gain)):
            s=s+gain[i]
            li.append(s)
        return max(li)
        