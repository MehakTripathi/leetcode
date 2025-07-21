# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
     def sortedArrayToBST(self, nums):
        def buildBST(si, ei):
            if si > ei:
                return None  

            mid = (si + ei) // 2
            root = TreeNode(nums[mid])   

            root.left = buildBST(si, mid - 1)   
            root.right = buildBST(mid + 1, ei) 

            return root

        return buildBST(0, len(nums) - 1)

     
        