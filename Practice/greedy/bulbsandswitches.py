import sys

INF = 10 ** 9

def bulbsandswitches():
    N, current, target = parse_input()
    solve_bulbsandswitches(N, current, target)

def solve_bulbsandswitches(N, current, target):
    cache = {}

    visited = 0

    ret = INF

    for i in range(N):
        visited |= (1 << i)
        switch(current, i)
        ret = min(ret, 1 + dp(visited, current, target, cache))
        switch(current, i)
        visited &= ~(1 << i)

    print(ret)
    return ret

def dp(visited, current, target, cache):
    # print(current)
    if current == target:
        return 0

    if visited in cache:
        return cache[visited]

    ret = INF

    for i in range(len(current)):
        if (visited & (1 << i)) == 0:
            visited |= (1 << i)
            switch(current, i)
            ret = min(ret, 1 + dp(visited, current, target, cache))
            switch(current, i)
            visited &= ~(1 << i)

    cache[visited] = ret
    return ret

def switch(current, i):
    if i == 0:
        current[0] = (current[0] + 1) % 2
        current[1] = (current[1] + 1) % 2

    elif i == len(current) - 1:
        current[i]   = (current[i] + 1) % 2
        current[i-1] = (current[i-1] + 1) % 2

    else:
        current[i]   = (current[i] + 1) % 2
        current[i-1] = (current[i-1] + 1) % 2
        current[i+1] = (current[i+1] + 1) % 2
        

def parse_input():
    input = sys.stdin.readline  # fast input
    
    N = int(input().strip())
    
    # Since digits are given without spaces, read as string
    current = list(map(int, input().strip()))
    target = list(map(int, input().strip()))
    
    return N, current, target


# Example usage
if __name__ == "__main__":
    bulbsandswitches()