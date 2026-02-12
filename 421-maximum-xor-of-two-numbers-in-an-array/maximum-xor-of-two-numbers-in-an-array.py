class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask=0
        maxor=0
        for i in range(32,-1 ,-1):
            mask |= (1<<i)
            prefixs= {num & mask for num in nums}
            cand= maxor | (1<<i)
            for p in prefixs:
                if p^ cand in prefixs:
                    maxor |= cand
                    break
        return maxor
        