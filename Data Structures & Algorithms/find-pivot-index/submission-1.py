class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for pivot_index in range(len(nums)):
            #print(f'Pivot_index: {pivot_index}, lsum = {left_sum}, rsum = {total_sum - left_sum - nums[pivot_index]}')
            if (total_sum - left_sum - nums[pivot_index]) == left_sum:
                return pivot_index
            left_sum+=nums[pivot_index]
        return -1