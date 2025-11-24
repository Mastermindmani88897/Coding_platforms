class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans=[]
        s=''
        new=0
        for i in range(len(nums)):
            nums[i]=str(nums[i])
            s=s+nums[i]
            new=int(s,2)
            if new%5==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans