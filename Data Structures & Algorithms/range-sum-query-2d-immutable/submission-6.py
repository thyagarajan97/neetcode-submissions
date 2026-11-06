class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        #A single pass solution
        #Every cell on the sum matrix holds the sum of the 2d-array from 0,0
        #The right-corner of the array should hold the sum of that portion of the matrix
        self.sum_matrix = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        #print(self.sum_matrix)
        for i in range(1, len(self.sum_matrix)):
            og_i_index = i - 1
            for j in range(1, len(self.sum_matrix[0])):
                og_j_index = j - 1
                self.sum_matrix[i][j] = self.matrix[og_i_index][og_j_index] +\
                     self.sum_matrix[i-1][j] + self.sum_matrix[i][j-1] - self.sum_matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1 # Offsetting the values for sum matrix
        top_right = (row1-1, col2)
        bottom_right = (row2, col2)
        bottom_left = (row2, col1 - 1)
        upper_left_corner = (row1 - 1, col1 - 1)
        #print(f'Top-right: {top_right}')
        #print(f'Bottom-left: {bottom_left}')
        #print(f'Bottom-right: {bottom_right}')
        #print(f'Upper_left_corner: {upper_left_corner}')
        s_val = self.sum_matrix[bottom_right[0]][bottom_right[1]] - self.sum_matrix[top_right[0]][top_right[1]] -\
            self.sum_matrix[bottom_left[0]][bottom_left[1]] + self.sum_matrix[upper_left_corner[0]][upper_left_corner[1]]
        return s_val


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)