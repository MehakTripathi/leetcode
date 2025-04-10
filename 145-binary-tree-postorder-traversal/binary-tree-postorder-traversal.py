# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans=[]
        st1, st2=[root], []

        while st1:
            node=st1.pop()
            st2.append(node.val)

            if node.left:
                st1.append(node.left)
            if node.right:
                st1.append(node.right)
                
        return st2[::-1]


        '''ans=[]
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            ans.append(root.val)

        postorder(root)
        return ans'''
        