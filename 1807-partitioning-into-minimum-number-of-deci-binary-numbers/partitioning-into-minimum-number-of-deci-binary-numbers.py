class Solution:
    def minPartitions(self, n: str) -> int:
        li=[]
        li.extend(n)
        li1=[]
        for i in range(len(li)):
            li1.append(int(li[i]))
        return max(li1)