class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        len_flw = len(flowerbed)
        if n == 0:
            return True
        if len_flw == 1:
            if flowerbed[0] == 1:
                return False
            else:
                return True
        if len_flw > 1:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] == 1
                n-=1
            #end if
            if flowerbed[len_flw - 2] == 0 and flowerbed[len_flw - 1] == 0:
                flowerbed[len_flw - 1] == 1
                n-=1
            #end if
        #end if
        for r in range(1, len(flowerbed) - 1):
            if flowerbed[r-1] == 0 and flowerbed[r+1] == 0 and flowerbed[r] == 0:
                n-=1
                flowerbed[r]= 1
            #end if
        #end for
        if n<=0:
            return True
        else:
            return False