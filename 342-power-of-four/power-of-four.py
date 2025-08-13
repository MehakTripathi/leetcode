class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        power=1
        while (power<=n):
            if (power ==n):
                return True
            power *=4
        return False
        