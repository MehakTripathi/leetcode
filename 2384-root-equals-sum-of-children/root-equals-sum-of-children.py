# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        if not root:
            return True
        if root.val == root.left.val + root.right.val:
            return True
        else:
            return False
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        