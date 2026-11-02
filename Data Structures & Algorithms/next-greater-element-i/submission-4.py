class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [] # Creating a stack 
        #Creating a result-list for returning
        next_greater_elem = [-1] * len(nums2)
        nums2_hash_map = {}
        for i in range(len(nums2)-1, -1, -1):
            nums2_hash_map[nums2[i]] = i
            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                #print(f'popping - {val}')
            #end while
            if stack and nums2[i] < stack[-1]:
                next_greater_elem[i] = stack[-1]
            #end if
            stack.append(nums2[i])
            #print(f'Stack-State: {stack}')
        #end for
        return [next_greater_elem[nums2_hash_map[elem]] for elem in nums1]

            