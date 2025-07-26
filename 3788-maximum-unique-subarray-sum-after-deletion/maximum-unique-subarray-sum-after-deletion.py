class Solution(object):
    def maxSum(self, nums):
        nums= list(set(nums))
        ans=0
        nums.sort()
        for i in range(len(nums)-1, -1, -1):
            if ans+nums[i]> ans:
                ans+=nums[i]
            else:
                break
        return ans if ans!=0 else nums[len(nums)-1]
        """
        :type nums: List[int]
        :rtype: int
        """
        