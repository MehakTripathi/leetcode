# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.maxSum = float('-inf')
        def dfs(root):
            if root is None:
                return 0
            left = max(dfs(root.left),0)
            right= max(dfs(root.right), 0)

            self.maxSum = max( left+ right+root.val, self.maxSum)
            return max(left, right) + root.val
        dfs(root)
        return self.maxSum


        
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        