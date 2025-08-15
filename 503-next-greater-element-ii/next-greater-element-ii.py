class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        for i in range(n):
            for j in range(i+1, i+n):
                if nums[j % n] > nums[i]:
                    res[i] = nums[j % n]
                    break
        return res
