class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=0
        l=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j  and nums[j]<nums[i]:
                    c=c+1
            l.append(c)
            c=0
        return l
            
        