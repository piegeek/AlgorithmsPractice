def find (x, adj):
    if adj[x] == x:
        return x
    return find(adj[x], adj)

def union(a, b, adj):
    a = find(a, adj)
    b = find(b, adj)
    if a != b :
        adj[b] = a

def solution(N, info, game):
    result = 0

    adj = [0] * (N)

    for i in range(1, N):
        adj[i] = i

    for i in range(len(game)):
        first = game[i][0]
        for j in range(len(game[i])):
            union(first, game[i][j], adj)

    for i in range(len(game)):
        isChecked = True
        cur = game[i][0]
        for j in range(len(info[1])):
            if find(cur, adj) == find(info[1][j], adj):
                isChecked = False
                break
        if isChecked:
            result += 1

    return result
