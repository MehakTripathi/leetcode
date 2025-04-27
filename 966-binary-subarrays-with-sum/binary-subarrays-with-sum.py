from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            l,r= 0,0
            sum=0
            count= 0
            n= len(nums)

            if goal <0:
                return 0

            for r in range(n):
                sum += nums[r]   
                while sum > goal:
                    sum = sum- nums[l]
                    l= l+1
                count = count +(r-l+1)
                r=r+1
            return count
        return atMost(goal) - atMost(goal - 1)
        
        