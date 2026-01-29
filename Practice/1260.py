def main():
    data = list(map(int, input().split(" ")))
    num_nodes = int(data[0])
    num_edges = int(data[1])
    start_vert = int(data[2])

    edges = []
    vertices = []
	
    graph = [[] for _ in range(num_nodes)]

    for i in range(num_edges):
        data_sub = list(map(int, input().split(" ")))

        graph[data_sub[0]-1].append(data_sub[1])
        graph[data_sub[1]-1].append(data_sub[0])

    print(graph)

    visited = [False] * num_nodes
    visited[start_vert-1] = True

    print(1, end=" ")

    dfs(start_vert, graph, visited)

def dfs(vertex, graph, visited):
    for child in graph[vertex-1]:
        if visited[child-1] == False:
            visited[child-1] = True
            print(child, end=" ")
            dfs(child, graph, visited)
    


main()