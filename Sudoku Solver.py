from typing import List

def isValid(board: List[List[str]], row: int, col: int, c: str) -> bool:
    for i in range(9):
        if board[i][col] == c:
            return False
        if board[row][i] == c:
            return False
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
            return False
    return True

def solveSudoku(board: List[List[str]]) -> bool:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                for c in "123456789":
                    if isValid(board, i, j, c):
                        board[i][j] = c
                        if solveSudoku(board):
                            return True
                        else:
                            board[i][j] = "."
                return False
    return True




if __name__ == "__main__":
    board = [
        ["9", "5", "7", ".", "1", "3", ".", "8", "4"],
        ["4", "8", "3", ".", "5", "7", "1", ".", "6"],
        [".", "1", "2", ".", "4", "9", "5", "3", "7"],
        ["1", "7", ".", "3", ".", "4", "9", ".", "2"],
        ["5", ".", "4", "9", "7", ".", "3", "6", "."],
        ["3", ".", "9", "5", ".", "8", "7", ".", "1"],
        ["8", "4", "5", "7", "9", ".", "6", "1", "3"],
        [".", "9", "1", ".", "3", "6", ".", "7", "5"],
        ["7", ".", "6", "1", "8", "5", "4", ".", "9"],
    ]
    solveSudoku(board)
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()