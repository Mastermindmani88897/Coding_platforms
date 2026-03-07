class Solution:
    def noOfWays(self, m, n, x):
        dp=[0]*(x+1)
        dp[0]=1
        for _ in range(n):
            new=[0]*(x+1)
            for s in range(x+1):
                if dp[s]:
                    for f in range(1,m+1):
                        if s+f<=x:
                            new[s+f]+=dp[s]
            dp=new
        return dp[x]