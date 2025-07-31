# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def gene(s,e):
            if s>e:
                return [None,]

            all=[]
            for i in range(s,e+1):
                ltree = gene(s,i-1)
                rtree= gene(i+1,e)

                for a in ltree:
                    for b in rtree:
                        curr= TreeNode(i)
                        curr.left= a
                        curr.right= b
                        all.append(curr)

            return all
        return gene(1,n) if n else []

        