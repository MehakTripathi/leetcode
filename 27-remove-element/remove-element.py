class Solution(object):
    def removeElement(self, nums, val):
        n=len(nums)
        counter=0
        i = 0
        while i < len(nums):  
            if nums[i] == val:
                nums.pop(i)
                counter += 1
                
               
            else:
                i += 1
        return n-counter
       
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        