from collections import Counter

class Solution:
    def twoSum(self, arr, target):
        l = Counter(arr)
        for i in range(len(arr)):
            complement = target - arr[i]
            if complement in l:
                
                if complement == arr[i]:
                    if l[arr[i]] > 1:
                        return True
                else:
                    return True
        return False
