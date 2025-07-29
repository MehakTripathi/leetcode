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

        def mirror(root1,root2):
            if not root1 and not root2:
                return True 
            if not root1 and root2:
                return False
            if root1 and not root2:
                return False
            if root1.val== root2.val and mirror(root1.left, root2.right) and mirror(root1.right, root2.left):
                return True
            return False    
        return mirror(root.left, root.right)

       
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        