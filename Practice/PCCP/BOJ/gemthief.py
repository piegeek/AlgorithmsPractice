import sys
import heapq

def gemthief():
    N, K, jewels, bags = parse_input()
    solve_gemthief(N, K, jewels, bags)

def solve_gemthief(N, K, jewels, bags):
    # DFS sol
    # visited = [ False for _ in range(N) ]
    # depth = 0
    # ret = dfs(visited, depth, N, K, jewels, bags)

    # print(ret)
    # return ret

    # Greedy sol
    jewels = sorted(jewels, key = lambda x : x[0])
    bags = sorted(bags)
    filled = [ False for _ in range(K) ]
    heap = []

    for i in range(len(jewels)):
        m, v = jewels[i]
        bag_idx = -1

        # Find bag of minimum capacity that fits gem
        for j in range(K):
            if filled[j] == False and m <= bags[j]:
                bag_idx = j
                break

        # We cant put in object i
        if bag_idx == -1:
            continue
        else:
            filled[bag_idx] = True
            heapq.heappush(heap, (v, jewels[i]))

        if len(heap) > K:
            heapq.heappop(heap) 

    prices = [ x[0] for x in heap ]
    ret = sum(prices)
    print(ret)
    return ret


def dfs(visited, depth, N, K, jewels, bags):
    if depth == K:
        return 0

    ret = 0

    for i in range(N):
        if visited[i] == False and jewels[i][0] <= bags[depth]:
            visited[i] = True
            ret = max(ret, jewels[i][1] + dfs(visited, depth+1, N, K, jewels, bags))
            visited[i] = False

    return ret

def parse_input():
    input = sys.stdin.readline  # fast I/O
    
    N, K = map(int, input().split())
    
    jewels = []
    for _ in range(N):
        M, V = map(int, input().split())
        jewels.append((M, V))
    
    bags = []
    for _ in range(K):
        C = int(input().strip())
        bags.append(C)
    
    return N, K, jewels, bags


# Example usage
if __name__ == "__main__":
    gemthief()