# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return 
        arr=[]    
        def preorder(root,arr):
            if not root:
                return

            arr.append(root.val)
            preorder(root.left, arr)
            preorder(root.right, arr)
            return arr
        arr= preorder(root,arr)
        root.val=arr[0]
        curr=root
        for i in range(1, len(arr)):
            curr.left =None
            curr.right= TreeNode(arr[i])
            curr=curr.right
        """
        Do not return anything, modify root in-place instead.
        """
        