import sys

def countingtilings():
    n, m = parse_input()
    solve_countingtilings(n, m)

def solve_countingtilings(n, m):
    ret = dp(n, m)
    print(ret)
    return ret

def dp(n, m):
    if n == 2:
        return fib(m)

    if n == 1:
        return 1 if m % 2 == 0 else 0

    ret = 0

    if n % 2 == 0:
        ret = dp(n - 2, m) * dp(2, m)
        if m % 2 == 0:
            for i in range(2, m+1, 2):
                ret += choose(m, i)

        else:
            for i in range(1, m+1, 2):
                ret += choose(m, i)

    else:
        ret = dp(n - 1, m) * dp(1, m)
        if m % 2 == 0:
            for i in range(2, m+1, 2):
                ret += choose(m, i)
        else:
            pass

    return ret

def fib(m):
    if m == 1:
        return 1
    if m == 2:
        return 2

    else:
        return fib(m - 1) + fib(m - 2)

def choose(n, k):
    return fact(n) / (fact(k) * fact(n-k))

def fact(n):
    if n in [0, 1]:
        return 1

    return n * fact(n-1)

def parse_input():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    
    return n, m


if __name__ == "__main__":
    countingtilings()