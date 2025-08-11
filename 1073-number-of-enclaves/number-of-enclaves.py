class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        count=0
        m,n = len(grid), len(grid[0])
        def dfs(i,j):
            if i<0 or i>= m or j<0 or j>=n or grid[i][j]==0:
                return        
            grid[i][j]=0
            dfs(i,j +1)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i-1, j)
        for i in range(m):
            for c in [0,n-1]:
                if grid[i][c]==1:
                    dfs(i,c)

        
        for c in range(n):
            for r in [0, m-1]:
                if grid[r][c] ==1:
                    dfs(r,c)

        for row in range(1, m-1):
            for col in range(1, n-1):
                if grid[row][col]:
                    count+=1
        return count
    