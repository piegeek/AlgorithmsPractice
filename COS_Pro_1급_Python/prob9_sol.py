def solution(N, info, game):
    knows = info[1]
    
    for i in range(len(game)):
        for j in range(len(knows)):
            if knows[j] in game[i]:
                for k in range(len(game[i])):
                    knows.append(game[i][k])
                    
    result = 0
    
    for i in range(len(game)):
        in_game = False
        for j in range(len(game[i])):
            if game[i][j] in knows:
                in_game = True
                break
            
        if in_game == False:
            result += 1
    
    return result


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
