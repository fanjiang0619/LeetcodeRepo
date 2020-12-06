class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for i in range(9)]
        col = [{} for i in range(9)]
        box = [{} for i in range(9)]
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != ".":
                    row[r][num] = row[r].get(num, 0) + 1
                    print(row)
                    col[c][num] = col[c].get(num, 0) + 1
                    idx = r // 3 * 3 + c // 3
                    box[idx][num] = box[idx].get(num, 0) + 1
                    
                    if row[r][num] > 1 or col[c][num] > 1 or box[idx][num] > 1:
                        return False
        return True