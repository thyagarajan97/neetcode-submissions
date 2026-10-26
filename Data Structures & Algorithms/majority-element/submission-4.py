class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Brute force
        from collections import Counter
        freq_dict = Counter(nums)
        #Uses a heap data-structure to get the top-K elements by first consructing a heap and then getting the elements    
        import heapq
        #Reversing the dict; key = frequency, value is the actual element
        elem_tuple = [(v,k) for k,v in freq_dict.items()]
        #print(elem_tuple)
        #Heapify can take in a input as a tuple
        #O(n) complexity
        heapq.heapify(elem_tuple)
        #O(n * logn) where n is the num of elements we need to search
        #Here there is no need to search the entire heap for smaller values
        
        return heapq.nlargest(1, elem_tuple)[0][1]