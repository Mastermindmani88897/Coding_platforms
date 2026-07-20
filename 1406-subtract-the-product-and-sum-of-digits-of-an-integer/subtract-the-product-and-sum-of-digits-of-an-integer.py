class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        pr=1
        n1=0
        while(n!=0):
            n1=n%10
            pr=pr*n1
            s=s+n1
            n=n//10
        return (pr-s)