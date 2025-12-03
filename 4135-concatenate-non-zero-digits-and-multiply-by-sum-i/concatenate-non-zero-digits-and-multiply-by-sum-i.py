class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        n=str(n)
        st=''
        for i in range(len(n)):
            if n[i]!='0':
                st=st+n[i]

        print(st)
        s=0
        for i in range(len(st)):
            s=s+int(st[i])
        return s*int(st,10)
