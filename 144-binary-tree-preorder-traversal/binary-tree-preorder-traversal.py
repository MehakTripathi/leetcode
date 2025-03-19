# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
         
        if not root:
            return ans

        s=[root]
        while s:
            node= s.pop()
            ans.append(node.val)

            if node.right:
                s.append(node.right)

            if node.left:
                s.append(node.left)

        return ans


        '''def pre(root,arr):
            if root:
                arr.append(root.val)
                pre(root.left, arr)
                pre(root.right, arr)
        arr=[]
        pre(root,arr)
        return arr'''
                


        