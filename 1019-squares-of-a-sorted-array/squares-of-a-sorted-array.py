class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] *=nums[i]
        nums.sort()
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        