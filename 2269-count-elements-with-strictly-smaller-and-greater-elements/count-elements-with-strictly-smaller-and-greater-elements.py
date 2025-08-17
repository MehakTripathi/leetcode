class Solution:
    def countElements(self, nums: List[int]) -> int:
        mn, mx = min(nums), max(nums)
        count=0

        for i in nums:
            if mn < i < mx:
                count+=1
        return count

        