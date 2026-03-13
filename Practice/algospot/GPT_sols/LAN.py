def solve_LAN(N, xs, ys, edges):
	# Kruskal's Algorithm - Greedy

    parent = list(range(N))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a,b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    # existing cables
    for a,b in edges:
        union(a,b)

    all_edges = []

    for i in range(N):
        for j in range(i+1, N):
            dist = ((xs[i]-xs[j])**2 + (ys[i]-ys[j])**2)**0.5
            all_edges.append((dist, i, j))

    all_edges.sort()

    ans = 0

    for w,u,v in all_edges:
        if find(u) != find(v):
            union(u,v)
            ans += w

    print(ans)