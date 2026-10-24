class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Trying to optimize using 2 pointers since array is sorted
        l = 0
        r = len(numbers) - 1
        while True:
            if (numbers[l] + numbers[r]) == target:
                return [l + 1, r + 1]
            elif (numbers[l] + numbers[r]) > target:
                r-=1
            else:
                l+=1
        #end while

