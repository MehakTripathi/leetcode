# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check (self, root):
        if not root:
            return 0
            
        l= self.check(root.left)
        if l == -1:
            return -1
        r= self.check(root.right)
        if r== -1:
            return -1
        if abs(l-r) > 1:
            return -1
        return max(l,r) +1
        

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check(root) != -1
        