import sys

INF = 10 ** 9

def nthlon():
    test_cases = parse_input()

    for i, (M, events) in enumerate(test_cases, 1):
        solve_nthlon(M, events)

def solve_nthlon(M, events):
    max_sum = max(sum([x[0] for x in events]), sum([x[1] for x in events]))

    ret = dp(0, 0, [], M, events, max_sum)

    if ret == INF:
        print('IMPOSSIBLE')
    else:
        print(ret)
    return ret

def dp(idx, count, path, M, events, max_sum):
    sum_1 = sum([events[x][0] for x in path])
    if sum_1 >= max_sum or idx == M:
        # print(path)

        sum_1 = sum([events[x][0] for x in path])
        sum_2 = sum([events[x][1] for x in path])

        if sum_1 == sum_2 and sum_1 != 0:
            return 0
        else:
            return INF

    # Take idx
    path.append(idx)
    ret = events[idx][0] + dp(idx, count+1, path, M, events, max_sum)
    path.pop(-1)

    # Take idx + 1
    if idx + 1 < M:
        path.append(idx+1)
        ret = min(ret, events[idx+1][0] + dp(idx+1, count+1, path, M, events, max_sum))
        path.pop(-1)

    # Skip idx
    ret = min(ret, dp(idx+1, count, path, M, events, max_sum))

    return ret

def parse_input():
    input = sys.stdin.readline

    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        M = int(input().strip())

        events = []
        for _ in range(M):
            a, b = map(int, input().split())
            events.append((a, b))

        test_cases.append((M, events))

    return test_cases


# Example usage
if __name__ == "__main__":
    nthlon()