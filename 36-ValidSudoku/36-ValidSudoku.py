# Last updated: 5/31/2026, 11:36:04 PM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                k = (r // 3) * 3 + (c // 3)
                
                if val in rows[r] or val in cols[c] or val in boxes[k]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[k].add(val)
                
        return True