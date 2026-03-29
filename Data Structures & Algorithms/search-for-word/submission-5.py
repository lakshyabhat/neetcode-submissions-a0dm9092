class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        max_col = len(board[0])
        max_row = len(board)
        path = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                if Solution.dfs(r,c,0, word,max_row, max_col, board, path):
                    return True
        
        return False

    def dfs(row,col,w, word, max_row, max_col, board,path):

        if len(word) == w:
            return True

        if row >= max_row or col >= max_col or row<0 or col<0 or (row,col) in path or board[row][col]!=word[w]:
            return False
        
        path.add((row,col))
        if (Solution.dfs(row+1,col,w+1, word, max_row, max_col, board,path) or 
                Solution.dfs(row,col+1,w+1, word, max_row, max_col, board, path) or 
                Solution.dfs(row-1,col,w+1, word, max_row, max_col, board, path) or 
                Solution.dfs(row,col-1,w+1, word, max_row, max_col, board, path)):
                return True

        path.remove((row,col))
            
        return False
