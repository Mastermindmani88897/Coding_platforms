from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        
        max_val = max(nums)
        spf = list(range(max_val + 1))
        
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        def is_prime(x):
            return x > 1 and spf[x] == x
        
        prime_to_indices = defaultdict(list)
        
        for i, v in enumerate(nums):
            x = v
            factors = set()
            
            while x > 1:
                p = spf[x]
                factors.add(p)
                while x % p == 0:
                    x //= p
            
            for p in factors:
                prime_to_indices[p].append(i)
        
        q = deque([0])
        dist = [-1] * n
        dist[0] = 0
        
        used_prime = set()
        
        while q:
            i = q.popleft()
            
            if i == n - 1:
                return dist[i]
            
            if i - 1 >= 0 and dist[i - 1] == -1:
                dist[i - 1] = dist[i] + 1
                q.append(i - 1)
            
            if i + 1 < n and dist[i + 1] == -1:
                dist[i + 1] = dist[i] + 1
                q.append(i + 1)
            
            v = nums[i]
            
            if is_prime(v) and v not in used_prime:
                for nei in prime_to_indices[v]:
                    if dist[nei] == -1:
                        dist[nei] = dist[i] + 1
                        q.append(nei)
                
                used_prime.add(v)
        
        return -1