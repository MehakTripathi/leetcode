class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        Lsum, Rsum, maxlen = 0,0,0
        for i in range (k):
            Lsum += nums[i]
        maxlen = Lsum
        r= len(nums)-1
        for i in range(k-1, -1, -1):
            Lsum = Lsum - nums[i]
            Rsum= Rsum + nums[r]
            maxlen = max(maxlen, Lsum+ Rsum)
            r= r-1
        return maxlen
        