class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        for r in range(1, len(flowerbed) - 1):
            if flowerbed[r] == 0 and flowerbed[r-1] == 0 and flowerbed[r+1] == 0:
                n-=1
                flowerbed[r]= 1
            #end if
        #end for
        if n<=0:
            return True
        else:
            return False