class Solution:
    def isHappy(self, n: int) -> bool:
        if n<=0:
            return False
        res=n
        while res!=1 and res!=4:
            re=0
            while res!=0:
                n1=res%10
                re+=n1**2
                res//=10
            res=re
        return res==1
            
