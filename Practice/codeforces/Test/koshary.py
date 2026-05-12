def koshary():
    C, test_cases = parse_input()
    for i in range(C):
        x, y = test_cases[i]
        solve_koshary(x, y)

def solve_koshary(x, y):
    moves = [
        [2, 0],
        [0, 2]
    ]

    short_moves = [
        [1, 0],
        [0, 1]
    ]

    ret = False

    for move in moves:
        dx, dy = move
        ret = ret or dfs(dx, dy, False, moves, short_moves, x, y)

    for smove in short_moves:
        dx, dy = smove
        ret = ret or dfs(dx, dy, True, moves, short_moves, x, y)

    if ret == True:
        print('YES')
    else:
        print('NO')

def dfs(x, y, smove_used, moves, short_moves, goal_x, goal_y):
    if x == goal_x and y == goal_y:
        return True

    if x > 10 or y > 10:
        return False

    ret = False

    for move in moves:
        dx, dy = move
        ret = ret or dfs(x + dx, y + dy, smove_used, moves, short_moves, goal_x, goal_y)

    if smove_used == False:
        for smove in short_moves:
            dx, dy = smove
            ret = ret or dfs(x + dx, y + dy, True, moves, short_moves, goal_x, goal_y)

    return ret


def parse_input():
    C = int(input())

    test_cases = []

    for _ in range(C):
        test_cases.append(list(map(int, input().split())))

    return C, test_cases

if __name__ == '__main__':
    koshary()