class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=Counter(nums)
        s=[]
        for i in nums:
            if l[i]==2:
                s.append(i)
        s=list(set(s))
        return s
