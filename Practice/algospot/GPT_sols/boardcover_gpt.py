def boardcover():
    test_cases = parse_input()

    for H, W, board in test_cases:
        count = [0]
        solve_boardcover(H, W, board, count)
        print(count[0])


def solve_boardcover(H, W, board, count):
    # Find first empty cell
    found = False
    for i in range(H):
        for j in range(W):
            if board[i][j] == '.':
                found = True
                break
        if found:
            break

    # Base case: fully covered
    if not found:
        count[0] += 1
        return True

    any_success = False

    for block in get_available_blocks(board, i, j):
        # Place block
        for r, c in block:
            board[r][c] = '#'

        if solve_boardcover(H, W, board, count):
            any_success = True

        # Backtrack
        for r, c in block:
            board[r][c] = '.'

    return any_success


def get_available_blocks(board, i, j):
    blocks = []
    H = len(board)
    W = len(board[0])

    # 4 possible L-shaped blocks
    shapes = [
        [(0, 0), (1, 0), (0, 1)],
        [(0, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (1, 1)],
        [(0, 0), (1, 0), (1, -1)],
    ]

    for shape in shapes:
        coords = []
        valid = True
        for dr, dc in shape:
            r = i + dr
            c = j + dc
            if r < 0 or r >= H or c < 0 or c >= W or board[r][c] != '.':
                valid = False
                break
            coords.append((r, c))
        if valid:
            blocks.append(coords)

    return blocks


def parse_input():
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        H, W = map(int, input().split())
        board = [list(input().strip()) for _ in range(H)]
        test_cases.append((H, W, board))

    return test_cases


if __name__ == '__main__':
    boardcover()
