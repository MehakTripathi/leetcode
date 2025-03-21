class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
            res=[]
            stack= [(0,[0])]
            while stack:
                node,path=stack.pop()
                if node == len(graph)-1:
                    res.append(path)
                else:
                    for ngh in graph[node]:
                        stack.append((ngh,path+[ngh]))
            return res

