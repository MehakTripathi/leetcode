# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        
        if not root:
            return []

        stack1=[]
        cur= root
        while cur or stack1:
            while cur:
                stack1.append(cur)
                cur= cur.left
            cur= stack1.pop()
            res.append(cur.val)
            cur= cur.right
        return res
        



        '''ans=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
            
        inorder(root)
        return ans'''



            



        