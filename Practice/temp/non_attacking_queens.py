def nonAttackingQueens(n):
    # Write your code here.
    # Base cases
    if n in [0, 2, 3] : return 0
    if n == 1: return 1
    
    board = [ [ False for j in range(n) ] for i in range(n) ]

    possible = []

    count = 0
    
    for i in range(n):
        for j in range(n):
            board = [ [ False for j in range(n) ] for i in range(n) ]
            branches = []
            try_queen(board, i, j, 1, [], branches)

            print(branches)

            for branch in branches:
                if len(branch) == n and sorted(branch) not in possible:
                    possible.append(sorted(branch))
                    count += 1

    # print(possible)

    return count

def try_queen(board, i, j, num, stack, flush):
    stack.append([i, j])
    
    if num >= len(board):
        hold = []

        for s in stack:
            hold.append(s)

        stack = stack[:-1]

        flush.append(hold)
        return

    print(f'board before: {board}')
    
    fill_diagonal(board, i, j, True)
    fill_vertical(board, i, j, True)
    fill_horizontal(board, i, j, True)

    print(f'board after: {board}')

    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == False:
                try_queen(board, r, c, num+1, stack, flush)

                fill_diagonal(board, r, c, False)
                fill_vertical(board, r, c, False)
                fill_horizontal(board, r, c, False)

                for coord in stack:
                    fill_diagonal(board, coord[0], coord[1], True)
                    fill_vertical(board, coord[0], coord[1], True)
                    fill_horizontal(board, coord[0], coord[1], True)
                

def fill_diagonal(board, i, j, flag):
    i_0, j_0 = i, j
    
    # Lower right
    while i <= len(board) - 1 and j <= len(board[0]) - 1:
        board[i][j] = flag
        i += 1
        j += 1

    i, j = i_0, j_0

    # Lower left
    while i <= len(board) - 1 and j >= 0:
        board[i][j] = flag
        i += 1
        j -= 1

    i, j = i_0, j_0
        
    # Upper left
    while i >= 0 and j >= 0:
        board[i][j] = flag
        i -= 1
        j -= 1

    i, j = i_0, j_0

    # Upper right
    while i >= 0 and j <= len(board[0]) - 1:
        board[i][j] = flag
        i -= 1
        j += 1


def fill_vertical(board, i, j, flag):
    i_0, j_0 = i, j
    
    # Up
    while i >= 0:
        board[i][j] = flag
        i -= 1

    i, j = i_0, j_0

    # Down
    while i <= len(board) - 1:
        board[i][j] = flag
        i += 1

def fill_horizontal(board, i, j, flag):
    i_0, j_0 = i, j

    # Right
    while j <= len(board[0]) - 1:
        board[i][j] = flag
        j += 1

    i, j = i_0, j_0

    # Left
    while j >= 0:
        board[i][j] = flag
        j -= 1


if __name__ == "__main__":
   n = int(input())

   print(nonAttackingQueens(n))