class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        li=[]
        for i in range(len(nums)):
            if nums[i]==target:
                li.append(i)
        print(li)
        s=max(li)
        sa=[]
        for i in range(len(li)):
            sa.append(abs(li[i]-start))
        return min(sa)