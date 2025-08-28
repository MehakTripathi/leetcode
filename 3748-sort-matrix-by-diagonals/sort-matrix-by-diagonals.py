class Solution:
  def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
    diagonals = defaultdict(list)
    n = len(grid)

    for r in range(n):
      for c in range(n):
        diagonals[r - c].append(grid[r][c])

    for i in diagonals:
      diagonals[i].sort(reverse=(i >= 0))

    for r in range(n):
      for c in range(n):
        grid[r][c] = diagonals[r - c].pop(0)
        
    return grid