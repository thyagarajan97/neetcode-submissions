class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Brute-force
        #pop and then append
        for i in range(k):
            nums.insert(0, nums.pop())
        #end for
            
        