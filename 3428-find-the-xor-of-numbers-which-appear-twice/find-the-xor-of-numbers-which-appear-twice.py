class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        li=[]
        for i in range(len(nums)):
            if nums.count(nums[i])==2:
                li.append(nums[i])
        li=list(set(li))
        su=0
        for i in range(len(li)):
            su=su^li[i]
        return su