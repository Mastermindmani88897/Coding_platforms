class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        n=len(words)
        l=[]
        for i in range(n):
            s=0
            for j in range(len(words[i])):
                s+=weights[ord(words[i][j])-97]
            l.append(s%26)
        st=''
        for i in l:
            st+=chr(122-i)
        return st