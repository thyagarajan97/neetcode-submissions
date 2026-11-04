class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hash_set = set([i for i in range(1, len(grid)*len(grid) + 1)])
        repeating_num = -1
        for i in range(len(grid)):
            for j in range(len(grid)):
                val = grid[i][j]
                if val in hash_set:
                    hash_set.discard(val)
                else:
                    repeating_num = val
                #end if
            #end for
        #end for
        return [repeating_num, list(hash_set)[0]]
