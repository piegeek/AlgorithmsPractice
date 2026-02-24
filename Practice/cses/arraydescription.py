import sys

sys.setrecursionlimit(10 ** 6)

def arraydescription():
    n, m, arr = parse_input()
    solve_arraydescription(n, m, arr)

def solve_arraydescription(n, m, arr):
    # If given array doesn't meet specifications
    for i in range(n - 1):
        if arr[i] != 0 and arr[i+1] != 0 and abs(arr[i+1] - arr[i]) > 1:
            print(0)
            return 0

    ret = dfs(n, m, arr)

    print(ret)
    return ret

def dfs(n, m, arr):
    filled = True

    for idx in range(n):
        if arr[idx] == 0:
            filled = False
            i = idx
            break

    if filled:
        # print(arr)
        return 1

    count = 0

    left = []
    right = []

    cand = []

    if len(arr) == 1:
        return m

    if i > 0:
        if arr[i - 1] != 0:
            left = [ arr[i-1] - 1, arr[i-1], arr[i-1] + 1 ]
        else:
            left = [ x for x in range(1, m+1) ]

    if i < n - 1:
        if arr[i + 1] != 0:
            right = [ arr[i+1] - 1, arr[i+1], arr[i+1] + 1 ]
        else:
            right = [ x for x in range(1, m+1) ]

    if len(left) > 0 and len(right) > 0:
        for j in range(len(left)):
            for k in range(len(right)):
                if left[j] == right[k] and left[j] not in cand:
                    cand.append(left[j])

    elif len(left) == 0:
        cand = right
    elif len(right) == 0:
        cand = left

    # print(f'arr: {arr}, cand: {cand}')

    for c in cand:
        if 1 <= c and c <= m:
            arr[i] = c
            count += dfs(n, m, arr)
            
    # Backtracking - why always backtracking produces correct results and not only if count == 0?
    # if count == 0:
    #     arr[i] = 0
    arr[i] = 0
                    
    return count

def parse_input():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    return n, m, arr


if __name__ == "__main__":
    arraydescription()