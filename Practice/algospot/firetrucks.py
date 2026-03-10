import sys
import heapq

INF = 10 ** 9

def firetrucks():
    test_cases = parse_input()

    for i, (V, E, n, m, adj_list, fires, stations) in enumerate(test_cases, 1):
        solve_firetrucks(V, E, n, m, adj_list, fires, stations)

def solve_firetrucks(V, E, n, m, adj_list, fires, stations):
    # DFS sol -> Recursive dp; Iterative dp version is Bellman-Ford algorithm
    # time_sum = 0

    # # print(adj_list)

    # for fire in fires:
    #     visited = (1 << fire)

    #     ret = INF

    #     for edge in adj_list[fire]:
    #         b, t = edge
    #         visited |= (1 << b)
    #         ret = min(ret, t + dfs(b, visited, V, adj_list, fires, stations))
    #         visited &= ~(1 << b)

    #     # print(f'fire: {fire}, ret: {ret}')

    #     time_sum += ret

    # print(time_sum)
    # return time_sum

    # Dijkstra sol
    time_sum = 0

    for fire in fires:
        distances = [ INF for _ in range(V) ]
        distances[fire] = 0
        dijkstra(fire, distances, adj_list, V, fires, stations)

        time_sum += ret

    print(time_sum)
    return time_sum

def dijkstra(origin, distances, adj_list, V, fires, stations):
    queue = []

    for edge in adj_list[origin]:
        b, t = edge
        heapq.heappush(queue, (t, origin))

    while len(queue) > 0:
        dist, prev = heapq.heappop(queue)

        distances[node] = min(distances[node], dist + distances[prev])

        # for edge in adj_list[prev]:
        #     b, t = edge
        #     heapq.heappush(queue, ())

        pass
        

def dfs(last, visited, V, adj_list, fires, stations):
    if last in stations:
        return 0

    ret = INF

    for edge in adj_list[last]:
        b, t = edge
        if not (visited & (1 << b)):
            visited |= (1 << b)
            ret = min(ret, t + dfs(b, visited, V, adj_list, fires, stations))
            visited &= ~(1 << b)

    return ret

def parse_input():
    input = sys.stdin.readline

    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        V, E, n, m = map(int, input().split())

        adj_list = [ [] for _ in range(V) ]
        for _ in range(E):
            a, b, t = map(int, input().split())
            # Zero-indexing
            a = a - 1 
            b = b - 1
            adj_list[a].append([b, t])
            adj_list[b].append([a, t])

        # Zero-indexing
        fires = [x-1 for x in list(map(int, input().split()))]
        stations = [x-1 for x in list(map(int, input().split()))]

        test_cases.append((V, E, n, m, adj_list, fires, stations))

    return test_cases


# Example usage
if __name__ == "__main__":
    firetrucks()