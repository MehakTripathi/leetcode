class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return nums1

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return nums1

        del nums1[m:]

        for j in range(n):
            nums1.append(nums2[j])
        nums1.sort()

        return nums1
