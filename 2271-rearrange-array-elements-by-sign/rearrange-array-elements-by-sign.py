class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        nums.clear()
        for i in range(len(p)):
            nums.append(p[i])
            nums.append(n[i])
        return nums