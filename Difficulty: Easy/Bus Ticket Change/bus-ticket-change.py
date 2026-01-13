class Solution:
    def canServe(self, arr):
        fives=0
        tens=0
        for x in arr:
            if x==5:
                fives+=1
            elif x==10:
                if fives==0:
                    return False
                fives-=1
                tens+=1
            else:
                if tens>0 and fives>0:
                    tens-=1
                    fives-=1
                elif fives>=3:
                    fives-=3
                else:
                    return False
        return True
