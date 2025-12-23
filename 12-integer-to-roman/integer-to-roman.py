class Solution:
    def intToRoman(self, n: int) -> str:
        s=''
        while n//1000>0:
            s=s+'M'
            n=n-1000
        while n//900>0:
            s=s+'CM'
            n=n-900
        while n//500>0:
            s=s+'D'
            n=n-500
        while n//400>0:
            s=s+'CD'
            n=n-400
        while n//100>0:
            s=s+'C'
            n=n-100
        while n//90>0:
            s=s+'XC'
            n=n-90
        while n//50>0:
            s=s+'L'
            n=n-50
        while n//40>0:
            s=s+'XL'
            n=n-40
        while n//10>0:
            s=s+'X'
            n=n-10
        if n==9:
            s=s+'IX'
        elif n==8:
            s=s+'VIII'
        elif n==7:
            s=s+'VII'
        elif n==6:
            s=s+'VI'
        elif n==5:
            s=s+'V'
        elif n==4:
            s=s+'IV'
        elif n==3:
            s=s+'III'
        elif n==2:
            s=s+'II'
        elif n==1:
            s=s+'I'
        else:
            s=s
        return s
        
        