class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        ind=0
        s=''
        s+=num[::-1]
        for i in range(len(s)):
            if s[i]=='0':
                continue
            else:
                ind=i
                break

        print(ind)
        if ind==0:
            return num
        return num[:len(num)-ind]