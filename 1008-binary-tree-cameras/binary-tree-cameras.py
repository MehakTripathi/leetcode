# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        count = 0 

        def dfs(node):
            nonlocal count  
            if node is None: 
                return 1 
            
            lc = dfs(node.left)
            rc = dfs(node.right)

            if lc == -1 or rc == -1: 
                count += 1
                return 0 
            
            if lc == 0 or rc == 0: 
                return 1  
            
            return -1  

        if dfs(root) == -1:  
            count += 1
        
        return count
        
        

      

        

        