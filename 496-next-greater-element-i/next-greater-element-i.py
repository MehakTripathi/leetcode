class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n= len(nums1)
        mymap= { n: i for i, n in enumerate(nums1)}
        res= [-1]*n

        for i in range(len(nums2)):
            if nums2[i] not in mymap:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j]> nums2[i]:
                    idx = mymap[nums2[i]]
                    res[idx]= nums2[j]
                    break
        return res

        