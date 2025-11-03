from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n + 1)

        def f(i):
            # Base cases
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            # Recursive choices: take 1 step or 2 steps
            onestep = cost[i] + f(i + 1)
            twostep = cost[i] + f(i + 2)
            
            dp[i] = min(onestep, twostep)
            return dp[i]

        # You can start from either step 0 or step 1
        return min(f(0), f(1))
