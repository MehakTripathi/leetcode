# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        ans= 0
        d= deque([[root,1,0]])         #[node, num, level]
        prevlvl, prevnum= 0,1
        while d:
            node, num, lvl= d.popleft()
            if lvl> prevlvl:
                prevlvl = lvl
                prevnum = num

            ans = max(ans, num-prevnum+1)
            if node.left:
                d.append([node.left, 2*num, lvl+1])
            if node.right:
                d.append([node.right, 2*num+1, lvl+1])
        return ans
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        