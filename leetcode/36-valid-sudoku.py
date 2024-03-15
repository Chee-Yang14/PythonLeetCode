class Solution(object):
    def isValidSudoku(self, board):
        #check row to see if it contain any duplicate
        def is_valid_row(row):
            seen = set()
            for num in row:
                if num != '.' and num in seen:
                    return False
                seen.add(num)
            return True

        #check column to see if it contain any duplicate
        def is_valid_column(col):
            seen = set()
            for num in col:
                if num != '.' and num in seen:
                    return False
                seen.add(num)
            return True

        #check the 3x3 box to see if it contain any duplicate
        def is_valid_subbox(subbox):
            seen = set()
            for row in subbox:
                for num in row:
                    if num != '.' and num in seen:
                        return False
                    seen.add(num)
            return True
        #for loop naturally iterate in rows so we just check each row to see if it contain any dupicate
        for row in board:
            if not is_valid_row(row):
                return False

        #for loop use zip to check board in column instead to see if it contains any duplicate
        for col in zip(*board):
            if not is_valid_column(col):
                return False

        #iterate the 3x3 to check for any duplicate
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subbox = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not is_valid_subbox(subbox):
                    return False

        #if no false was triggered than it most likely true
        return True