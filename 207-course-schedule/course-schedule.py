class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list={i:[] for i in range(numCourses)} #making adjancecy list from edge list
        for dest,source in prerequisites:
            adj_list[source].append(dest)

        visited=set() # keeps track of nodes we’ve fully processed (DFS finished).
        recursion_stack=set()  #keeps track of nodes in the current DFS path for topological sort

        def dfs(u): #running dfs for toposort
            if u in recursion_stack: #already in the topo sort order so if found again it 
                return False #We found a back edge → there a cycle→topological sort is impossible.

            if u in visited:
                return True # base case for recursion so that it doesnt go to infinite loop
            recursion_stack.add(u) #add in the stack
            for v in adj_list[u]: #for child(neighbor) in adjancecy of u(parent) 
                if v not in visited:
                    if not dfs(v):
                        return False
            recursion_stack.remove(u) #no longer in current dfs path
            visited.add(u)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True



        



