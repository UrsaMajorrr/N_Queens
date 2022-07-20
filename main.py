N = 4


def solve_NQ(board, col):

    # all columns are full
    if col == N:
        return True

    for i in range(N):
        if safe(board, i, col):
            board[i][col] = 1
            if solve_NQ(board, col + 1):
                return True

        board[i][col] = 0

    return False


def safe(board, row, col):
    # check if row is safe
    for i in range(N):
        if board[row][i] == 1:
            return False

    # check if column is safe
    for i in range(N):
        if board[i][col] == 1:
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
