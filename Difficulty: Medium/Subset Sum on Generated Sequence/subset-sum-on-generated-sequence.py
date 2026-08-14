class Solution:
    def isPossible(self, arr, s, x):
        nums = []
        total = s

        nums.append(s)

        for a in arr:
            cur = total + a
            total += cur

            if cur <= x:
                nums.append(cur)
            else:
                break

        for v in reversed(nums):
            if v <= x:
                x -= v

            if x == 0:
                return True

        return False