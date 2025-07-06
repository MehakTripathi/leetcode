class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        sum = 0
        d = {0: 1}
        
        for num in nums:
            sum += num
            if (sum - k) in d:
                count += d[sum - k]
            if sum in d:
                d[sum] += 1
            else:
                d[sum] = 1
        return count
        



        '''n= len(nums)
        for s in range (n):
            sum=0
            for e in range(s,n):
                sum +=nums[e]
                if sum == k:
                    ans +=1
        return ans'''




        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        