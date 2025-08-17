class Solution:
    def new21Game(self, n: int, k: int, maxp: int) -> float:
        if k==0 or n>= k-1 + maxp:
            return 1.0

        dp=[0.0] * (n+1)
        dp[0]= 1.0
        wsum, probability= 1.0, 0.0

        for i in range(1,n+1):
            dp[i]= wsum / maxp
            if i< k:
                wsum+=dp[i]
            else:
                probability +=dp[i]
            if i>=maxp :
                wsum -=dp[i-maxp]
                
        return probability
        