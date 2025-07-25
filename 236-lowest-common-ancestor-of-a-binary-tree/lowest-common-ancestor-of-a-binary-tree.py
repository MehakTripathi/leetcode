# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return root
        if root == p or root== q:
            return root

        left= self.lowestCommonAncestor(root.left, p, q)
        right =self.lowestCommonAncestor(root.right, p, q)

        if left == None:
            return right
        elif right == None:
            return left
        else:
            return root
             

        

        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        