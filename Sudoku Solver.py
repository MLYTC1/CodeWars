def sudoku(puzzle):
    def face_control(n, r, c):
        if n in puzzle[r]:
            return False

        for i in range(9):
            if puzzle[i][c] == n:
                return False

        row, col = 3 * (r//3), 3 * (c//3)
        for i in range(row, row + 3):
            for j in range(col, col+3):
                if puzzle[i][j] == n:
                    return False
        return True

    def sol():
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for k in range(1, 10):
                        if face_control(k, i, j):
                            puzzle[i][j] = k
                            if sol():
                                return True
                    puzzle[i][j] = 0
                    return False
        return True

    sol()
    return puzzle
