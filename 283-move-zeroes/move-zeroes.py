class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonZero=0

        for i in range (len(nums)):
            if nums[i]!=0:
                nums[nonZero], nums[i]=nums[i], nums[nonZero]
                nonZero +=1
        """
        Do not return anything, modify nums in-place instead.
        """
        