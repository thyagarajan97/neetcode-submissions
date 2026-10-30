class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_dict = {}
        #next_elem = None
        for i in range(len(nums2)):
            j = i + 1
            while j < len(nums2) and nums2[j] < nums2[i]:
                j+=1
            #end while
            if j < len(nums2): next_dict[nums2[i]] = nums2[j]
        #end for
        #print(next_dict)
        return [next_dict.get(elem, -1) for elem in nums1]