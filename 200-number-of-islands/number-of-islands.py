from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
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
        return islands

        