from collections import  Counter
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        nums3=list(set(nums3))
        l1=Counter(nums1)
        l2=Counter(nums2)
        l3=Counter(nums3)
        l1.update(l2)
        l1.update(l3)
        li=[]
        for key,val in l1.items():
            if val>=2:
                li.append(key)
        return li

