class Solution:
    def findMaxProduct(self, arr):
        
        MOD = 10**9 + 7
        n = len(arr)
        
        if n == 1:
            return arr[0]
        
        neg_count = 0
        zero_count = 0
        max_neg = -11
        prod = 1
        
        for x in arr:
            if x == 0:
                zero_count += 1
            else:
                prod *= x
                if x < 0:
                    neg_count += 1
                    max_neg = max(max_neg, x)
        
        if zero_count == n:
            return 0
        
        if neg_count % 2:
            
            if neg_count == 1 and zero_count + 1 == n:
                return 0
            
            prod //= max_neg
        
        return prod % MOD if prod > 0 else prod