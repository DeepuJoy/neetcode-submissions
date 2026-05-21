class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Checking duplicates - use hash set - its a dictionary and hashmap combined together.

        cols = defaultdict(set)
        rows = defaultdict(set)
        grid = defaultdict(set) # key = (row / 3, col / 3)

        for r, row in enumerate(board):
            
            for c, col in enumerate(board):

                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in grid[r // 3, c // 3]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                grid[(r // 3, c // 3)].add(board[r][c])

        return True

                


        