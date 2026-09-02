class Solution:
    def solve(self, n, s):
        inside = set()
        rejected = set()
        occupied = 0
        ans = 0
    
        for ch in s:
            if ch not in inside and ch not in rejected:
                if occupied < n:
                    inside.add(ch)
                    occupied += 1
                else:
                    rejected.add(ch)
                    ans += 1
            else:
                if ch in inside:
                    inside.remove(ch)
                    occupied -= 1
                else:
                    rejected.remove(ch)
    
        return ans