N = 4


def solve_NQ(board, row, col):

    # all columns are full
    if col == N:
        return True

    # make current position a 1
    board[row][col] = 1

    if safe(board, row, col):
        row = 0
        if solve_NQ(board, row, col + 1):
            return True
    else:
        board[row][col] = 0
        if solve_NQ(board, row + 1, col):
            return True

    return False


def safe(board, row, col):
    # check if row is safe
    for i in range(N):
        if board[row][i] == 1 and i != col:
            return False

    # check if column is safe
    for i in range(N):
        if board[i][col] == 1 and i != row:
            return False

    # check if diagonal is safe
    return True


def print_board(board):
    for i in range(N):
        print(board[i], end=" ")
        print()


def create_board(dimension):
    board = [[0 for j in range(dimension)] for i in range(dimension)]
    return board


if __name__ == "__main__":
    board = create_board(N)
    solve_NQ(board, 0, 0)
