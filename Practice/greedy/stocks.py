# BOJ 11501
import sys
import heapq

def stocks():
    T, test_cases = parse_input()
    for N, prices in test_cases:
        solve_stocks(N, prices)

def solve_stocks(N, prices):
    queue = []

    profit = 0

    for i in range(N-1):
        if prices[i+1] < prices[i]:
            while len(queue) > 0 and queue[0] <= prices[i]:
                profit += prices[i] - heapq.heappop(queue) 

        else:
            heapq.heappush(queue, prices[i])

    while len(queue) > 0 and queue[0] <= prices[N-1]:
        profit += prices[N-1] - heapq.heappop(queue)

    print(profit)
    return profit

def parse_input():
    input = sys.stdin.readline  # fast input
    
    T = int(input().strip())
    test_cases = []
    
    for _ in range(T):
        N = int(input().strip())
        prices = list(map(int, input().split()))
        test_cases.append((N, prices))
    
    return T, test_cases


# Example usage
if __name__ == "__main__":
    stocks()