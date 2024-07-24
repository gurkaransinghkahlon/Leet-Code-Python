def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                current_char = board[i][j]
                if current_char != '.':
                    if(current_char + "found in row" + str(i) in seen or
                       current_char + "found in column" + str(j) in seen or
                       current_char + "found in box" + str(i//3) + " and " + str(j//3) in seen):
                       return False

                    seen.add(current_char + "found in row" + str(i))
                    seen.add(current_char + "found in column" + str(j))
                    seen.add(current_char + "found in box" + str(i//3) + " and " + str(j//3)) 

        return True