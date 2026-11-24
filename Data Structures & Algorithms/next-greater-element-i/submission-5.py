class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        monotonic_stack = []
        result_arr = [-1] * len(nums2)
        hash_map = dict()
        for i in range(len(nums2) -1 , -1, -1):
            hash_map[nums2[i]] = i
            while monotonic_stack and nums2[i] > nums2[monotonic_stack[-1]]:
                monotonic_stack.pop()
            if monotonic_stack:
                result_arr[i] = (monotonic_stack[-1])
            #end if
            monotonic_stack.append(i)
        #end for
        
        #print(result_arr)
        final_result = []
        for elem in nums1:
            if result_arr[hash_map[elem]] != -1:
                final_result.append(nums2[result_arr[hash_map[elem]]])
            else:
                final_result.append(-1)
        return final_result
