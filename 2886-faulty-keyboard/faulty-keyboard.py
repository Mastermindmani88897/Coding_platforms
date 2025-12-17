class Solution:
    def finalString(self, s: str) -> str:
        new=''
        for i in range(len(s)):
            if s[i]=="i":
                new=new[::-1]
            else:
                new=new+s[i]
        return new