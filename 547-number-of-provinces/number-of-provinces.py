class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i, vis):
            vis[i]=1
            for j in range(n):
                if isConnected[i][j] ==1 and vis[j]==0:
                    dfs(j,vis)

        n= len(isConnected)
        vis= [0]*n
        count=0

        for i in range(n):
            if not vis[i]:
                dfs(i,vis)
                count +=1
        return count
        