class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def dfs(ind, i, j, board, word):
            if ind == len(word):  # word is found
                return True
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[ind]:
                return False

            temp = board[i][j]
            board[i][j] = '#'  # mark as visited

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # four directions
                if dfs(ind + 1, i + dx, j + dy, board, word):
                    return True

            board[i][j] = temp  # backtrack
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(0, i, j, board, word):
                        return True
        return False
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        