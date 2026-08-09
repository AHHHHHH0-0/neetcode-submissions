class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n == ".":
                    continue
                elif n in row[i] or n in col[j] or n in square[(i//3)*3+j//3]:
                    return False
                row[i].add(n)
                col[j].add(n)
                square[(i//3)*3+j//3].add(n)
        return True
                    