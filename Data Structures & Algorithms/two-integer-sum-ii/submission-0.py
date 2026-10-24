class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(numbers):
            invert_sum = target - num
            if hash_map.get(invert_sum) is not None:
                return  [hash_map.get(invert_sum) + 1, index + 1]
            else:
                hash_map[num] = index
            #end if
        #end for

        