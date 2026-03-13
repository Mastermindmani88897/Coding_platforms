class Solution:
    def check(self, nums: List[int]) -> bool:
        se=[]
        l=[]
        for i in range(len(nums)):
            se=nums[i:]+nums[:i]
            l.extend(se)
            l.sort()
            print(se)
            print(l)
            if l==se:
                return True
            se=[]
            l=[]
        return False

