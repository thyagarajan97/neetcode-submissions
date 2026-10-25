class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sorting + 2 pointers
        nums.sort()
        #print(nums)
        ret_list = []
        #Fix the 1st number
        for i in range(len(nums)):
            if (i > 0) and (i < len(nums) - 1) and (nums[i] == nums[i-1]):
                continue
            l = i + 1
            r = len(nums) - 1
            #print(f'New iter: i {i}')
            while (l < r):
                current_sum = nums[i] + nums[l] + nums[r]
                    
                if current_sum == 0:
                    ret_list.append([nums[i], nums[l], nums[r]])
                    
                    # 1. Step both pointers inward first
                    l += 1
                    r -= 1
                    
                    # 2. Skip duplicates for the left pointer
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
                    # 3. Skip duplicates for the right pointer
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif current_sum > 0:
                    r -= 1
                else:
                    l+=1

            #end while
        return ret_list
        