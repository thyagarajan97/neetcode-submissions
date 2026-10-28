class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        for r in range(1, len(f) - 1):
            if f[r] == 0 and f[r-1] == 0 and f[r+1] == 0:
                n-=1
                f[r]= 1
            #end if
        #end for
        if n<=0:
            return True
        else:
            return False