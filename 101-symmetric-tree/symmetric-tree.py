# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.mirrorimg(root.left, root.right)

    def mirrorimg(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.mirrorimg(left.left, right.right) and self.mirrorimg(left.right, right.left)
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        