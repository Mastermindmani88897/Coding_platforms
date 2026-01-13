class Solution:
    def separateSquares(self, squares):
        total=0
        low=10**18
        high=0
        
        for _,y,l in squares:
            total+=l*l
            low=min(low,y)
            high=max(high,y+l)
        
        half=total/2
        
        def area_below(y):
            a=0
            for _,y0,l in squares:
                if y<=y0:
                    continue
                elif y>=y0+l:
                    a+=l*l
                else:
                    a+=(y-y0)*l
            return a
        
        for _ in range(60):
            mid=(low+high)/2
            if area_below(mid)<half:
                low=mid
            else:
                high=mid
        
        return low
