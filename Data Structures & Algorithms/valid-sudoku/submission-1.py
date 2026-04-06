class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            visit = set()
            for col in range(len(board[0])):
                if board[row][col]!='.' and board[row][col] in visit:
                    return False
                else:
                    visit.add(board[row][col])

        for col in range(len(board[0])):
            visit = set()
            for row in range(len(board)):
                if board[row][col] != '.' and board[row][col] in visit:
                    return False
                else:
                    visit.add(board[row][col])

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                visit = set()
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        if board[row][col] != '.' and board[row][col] in visit:
                            return False
                        else:
                            visit.add(board[row][col])
        return True