class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        parent = list(range(len(source)))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        for a, b in allowedSwaps:
            union(a, b)
        
        from collections import defaultdict, Counter
        
        groups = defaultdict(list)
        for i in range(len(source)):
            groups[find(i)].append(i)
        
        ans = 0
        
        for g in groups.values():
            count = Counter()
            
            for i in g:
                count[source[i]] += 1
            
            for i in g:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    ans += 1
        
        return ans