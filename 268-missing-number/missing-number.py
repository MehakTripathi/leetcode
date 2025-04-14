class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        v=[-1] * (n+1)
        for j in nums:
            v[j] = j
        for i in range(len(v)):
            if v[i] == -1:
                return i 
        return 0

        