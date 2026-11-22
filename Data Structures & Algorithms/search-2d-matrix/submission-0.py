class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Search which row can the element be in
        m = len(matrix) -1
        n = len(matrix[0]) -1
        result_row = -1
        l = 0
        r  = m
        while l<=r:
            mid = (l+r)//2
            if target >= matrix[mid][0] and target <= matrix[mid][n]:
                #Found the row
                result_row = mid
                break
            elif target > matrix[mid][n]:
                l=mid+1
            else:
                r=mid -1
        #end while 
        if result_row == -1:
            return False
        l = 0
        r  = n
        while l<=r:
            mid = (l+r)//2
            if matrix[result_row][mid] == target:
                #Found the row,col
                return True
            elif target > matrix[result_row][mid]:
                l=mid+1
            else:
                r=mid -1
        #end while 
        return False