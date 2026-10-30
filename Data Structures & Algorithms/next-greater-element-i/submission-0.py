class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_dict = {}
        for i in range(len(nums2)):
            j = i + 1
            while j < len(nums2):
                if nums2[j] > nums2[i]:
                    next_dict[nums2[i]] = nums2[j]
                    break
                j+=1
                #end if
            #end while
        #end for
        #print(next_dict)
        return [next_dict.get(elem, -1) for elem in nums1]