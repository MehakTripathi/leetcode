from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n =len(grid), len(grid[0])
        def dfs(i,j, visited):
            visited[i][j]= 1
            dir= [(1,0), (0,1), (-1, 0), (0,-1)]
            for nr, nc in dir:
                row, col = nr+i, nc+j
                if 0 <= row < m and 0 <= col < n and grid[row][col] == "1" and visited[row][col] == 0:
                    dfs(row, col, visited)

        island=0
        visited= [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] =="1" and visited[i][j]==0:
                    dfs(i,j,visited)
                    island +=1

        return island




        '''if not grid:
            return 0

        m= len(grid)
        n= len(grid[0])
        visit = set()
        islands = 0

        def bfs (r,c):
            q= deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions= [(1,0),(-1,0),(0,1),(0,-1)]
                for dr, dc in directions:
                    new_row, new_col = row+dr, col+dc
                    if (0<= new_row < m and 0 <= new_col < n) and grid[new_row][new_col] == "1" and (new_row, new_col) not in visit:
                        visit.add((new_row, new_col))
                        q.append(( new_row, new_col))

        for r in range(m):
            for c in range (n):
                if grid[r][c] =="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands +=1
        return islands'''


        