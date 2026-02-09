import sys
import heapq

def newgame2():
    N, K, board, horses = parse_input()
    solve_newgame2(N, K, board, horses)

def solve_newgame2(N, K, board, horses):
    moves = [
        [0, 1],
        [0, -1],
        [-1, 0],
        [1, 0]
    ]

    pos = [ [ [] for _ in range(N) ] for _ in range(N) ]

    # Initialize
    for horse in horses:
        i, r, c, d = horse
        pos[r][c].append(horse)

    for i in range(1, 1000+1):
        # print('------------')
        # for row in pos:
        #     print(row)
        # print('------------')
        if simulate_turn(N, K, board, pos, horses, moves) == True:
            print(i)
            return i

    print(-1)
    return -1

# GPT Fix: End immediately if after a move there are 4 horses stacked, typo issue in [r+dy][c+dx], only change direction of horse A when moving to a blue space
# ISSUE: Problem comprehension, Typo
def simulate_turn(N, K, board, pos, horses, moves):
    for k in range(K):
        horse = horses[k]
        i, r, c, d = horse

        move = moves[d-1]
        dy, dx = move

        game_end = False

        # White space
        if 0 <= r + dy and r + dy <= N-1 and 0 <= c + dx and c + dx <= N-1 and board[r+dy][c+dx] == 0:
            game_end = move_whitespace(r, c, dy, dx, pos, horse, horses)

        # Red space
        elif 0 <= r + dy and r + dy <= N-1 and 0 <= c + dx and c + dx <= N-1 and board[r+dy][c+dx] == 1:
            game_end = move_redspace(r, c, dy, dx, pos, horse, horses)

        # Blue space or horse moves out of board
        else:
            horse_idx = pos[r][c].index(horse)
            to_move = pos[r][c][horse_idx:]

            dy, dx = (-1) * dy, (-1) * dx

            horses[k][3] = get_opposite_dir(horses[k][3])

            # for horse_to_move in to_move:
            #     horse_to_move_idx = horses.index(horse_to_move)
            #     horses[horse_to_move_idx][3] = get_opposite_dir(horses[horse_to_move_idx][3])

            if 0 <= r + dy and r + dy <= N-1 and 0 <= c + dx and c + dx <= N-1 and board[r+dy][c+dx] == 0:
                game_end = move_whitespace(r ,c, dy, dx, pos, horse, horses)
            elif 0 <= r + dy and r + dy <= N-1 and 0 <= c + dx and c + dx <= N-1 and board[r+dy][c+dx] == 1:
                game_end = move_redspace(r, c, dy, dx, pos, horse, horses)
            else:
                pass

        if game_end:
            return True

    return False 

def get_opposite_dir(d):
    if d == 1:
        return 2
    elif d == 2:
        return 1
    elif d == 3:
        return 4
    elif d == 4:
        return 3

def move_whitespace(r, c, dy, dx, pos, horse, horses):
    horse_idx = pos[r][c].index(horse)
    to_move = pos[r][c][horse_idx:]

    pos[r][c] = pos[r][c][:horse_idx]
    pos[r+dy][c+dx] += to_move

    for horse_to_move in to_move:
        horse_to_move_idx = horses.index(horse_to_move)
        horses[horse_to_move_idx][1] = r + dy
        horses[horse_to_move_idx][2] = c + dx

    N = len(pos)

    for i in range(N):
        for j in range(N):
            if len(pos[i][j]) >= 4:
                return True

    return False
    

def move_redspace(r, c, dy, dx, pos, horse, horses):
    horse_idx = pos[r][c].index(horse)
    to_move = pos[r][c][horse_idx:]

    pos[r][c] = pos[r][c][:horse_idx]
    pos[r+dy][c+dx] += to_move[::-1]

    for horse_to_move in to_move:
        horse_to_move_idx = horses.index(horse_to_move)
        horses[horse_to_move_idx][1] = r + dy
        horses[horse_to_move_idx][2] = c + dx
    
    N = len(pos)

    for i in range(N):
        for j in range(N):
            if len(pos[i][j]) >= 4:
                return True

    return False


def parse_input():
    input = sys.stdin.readline

    N, K = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    horses = []
    for i in range(K):
        r, c, d = map(int, input().split())
        horses.append([i, r - 1, c - 1, d])  # convert to 0-based (row, col)

    return N, K, board, horses


# example usage
if __name__ == "__main__":
	newgame2()