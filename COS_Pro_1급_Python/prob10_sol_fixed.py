def solution(N, info, game):
    result = 0
    
    # Create adjacency list
    al = create_adjacency_list(N, game)
    
    print(al)
    
    # Run dfs to find all the candidates
    knows = info[1]
    
    for v in knows:
        visited = [False for i in range(N)]
        dfs(al, v, knows, visited)
        
    print(knows)
    
    # Traverse through games to find out which one can win
    for g in game:
        lose = False
        for x in g:
            if x in knows:
                lose = True
                break
            
        if not lose:
            result += 1
    
    return result
    
def dfs(al, v, knows, visited):
    if visited[v] == True:
        return
    
    visited[v] = True
    
    if v not in knows:
        knows.append(v)
    
    for vertex in al[v]:
        dfs(al, vertex, knows, visited)
    
def create_adjacency_list(N, game):
    al = [ [] for i in range(N) ]
    
    for g in game:
        if len(g) > 1:
            for i in range(len(g)):
                for j in range(len(g)):
                    if g[i] != g[j]:
                        if g[j] not in al[g[i]]:
                            al[g[i]].append(g[j])
                
    return al


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
N = 5
info = [[ 1 ], [ 4 ]]
game = [[1, 2], [3], [3, 4]]
ret = solution(N, info, game)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

N = 7
info = [[ 3 ], [ 1, 2, 3 ]]
game = [[1], [2], [3], [4], [5], [6], [4, 5], [3, 6]]
ret = solution(N, info, game)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
