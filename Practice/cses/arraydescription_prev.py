import sys

def arraydescription():
    n, m, arr = parse_input()
    solve_arraydescription(n, m, arr)

def solve_arraydescription(n, m, arr):
    count = [ 0 for _ in range(n) ]

    for i in range(n):
        if i == 0 and arr[i] == 0 and n >= 2:
            cand = [arr[i+1] - 1, arr[i+1], arr[i+1] + 1]
            for c in cand:
                if 1 <= c and c <= m:
                    count[i] += 1
        elif i == n - 1 and arr[i] == 0 and n >= 2:
            cand = [arr[i-1] - 1, arr[i-1], arr[i-1] + 1 ]
            for c in cand:
                if 1 <= c and c <= m:
                    count[i] += 1
        elif arr[i] == 0 and n >= 3:
            left_cand  = [arr[i-1] - 1, arr[i-1], arr[i-1] + 1]
            right_cand = [arr[i+1] - 1, arr[i+1], arr[i+1] + 1]

            cand = []

            for j in range(3):
                for k in range(3):
                    if left_cand[j] == right_cand[k] and left_cand[j] not in cand:
                        cand.append(left_cand[j])

            for c in cand:
                if 1 <= c and c <= m:
                    count[i] += 1

    ret = 1

    for cnt in count:
        if cnt > 0:
            ret *= cnt

    print(ret)
    return ret


def parse_input():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    return n, m, arr


if __name__ == "__main__":
    arraydescription()