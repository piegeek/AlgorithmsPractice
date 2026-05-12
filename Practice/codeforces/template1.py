import sys

def parse_input():
    input = sys.stdin.readline
    
    C = int(input())

    test_cases = []
    
    for _ in range(C):
        n = int(input())
        arr = list(map(int, input().split()))
        test_cases.append([n, arr])

    return C, test_cases