class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points_list = [i for i in range(len(points))]

        parents = [i for i in range(len(points))]

        ret = 0

        edges = []

        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    edges.append([i, j, abs(x2 - x1) + abs(y2 - y1)])


        edges = sorted(edges, key = lambda x : x[2])

        for edge in edges:
            v1, v2, cost = edge
            u = find(v1, parents)
            v = find(v2, parents)

            if u != v:
                union(v1, v2, parents)
                ret += cost

        return ret


def find(v, parents):
    while v != parents[v]:
        v = parents[v]

    return v

def union(u, v, parents):
    u = find(u, parents)
    v = find(v, parents)

    if u != v:
        parents[v] = u


        


        