class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(i, j, visited, word):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if (i,j) in visited:
                return False
            if board[i][j] != word[0]:
                return False

            visited.add((i,j))
            if len(word) == 1:
                return True

            found = any(check(next_i, next_j, visited, word[1:]) for next_i, next_j in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)])
            visited.remove((i,j))
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(i, j, set(), word):
                    return True
        return False