def count(i):
    li=[]
    i=str(i)
    li.extend(i)
    if len(li)%2!=0:
        return 0
    return 1
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            c+=count(i)
        return c