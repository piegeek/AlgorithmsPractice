import sys

def gearrotation():
    gears, rotations = parse_input()
    solve_gearrotation(gears, rotations)


def solve_gearrotation(gears, rotations):
    for idx, direction in rotations:
        # 1단계: 회전 방향 먼저 결정 (회전 전 상태 기준)
        directions = [0] * 4
        directions[idx] = direction
        
        # 왼쪽으로 전파
        for i in range(idx, 0, -1):
            if gears[i][6] != gears[i-1][2]:  # 극이 다르면
                directions[i-1] = -directions[i]
            else:
                break  # 같으면 전파 중단
        
        # 오른쪽으로 전파
        for i in range(idx, 3):
            if gears[i][2] != gears[i+1][6]:  # 극이 다르면
                directions[i+1] = -directions[i]
            else:
                break  # 같으면 전파 중단
        
        # 2단계: 모든 톱니바퀴 동시에 회전
        for i in range(4):
            if directions[i] == 1:  # 시계 방향
                gears[i] = [gears[i][-1]] + gears[i][:-1]
            elif directions[i] == -1:  # 반시계 방향
                gears[i] = gears[i][1:] + [gears[i][0]]
    
    # 점수 계산
    ret = sum(2**i for i in range(4) if gears[i][0] == 1)
    print(ret)
    return ret


def parse_input():
    input = sys.stdin.readline
    gears = []
    for _ in range(4):
        line = input().strip().split()
        if len(line) == 1:
            gears.append(list(map(int, line[0])))
        else:
            gears.append(list(map(int, line)))
    
    K = int(input().strip())
    rotations = []
    for _ in range(K):
        idx, direction = map(int, input().split())
        rotations.append((idx - 1, direction))
    
    return gears, rotations


if __name__ == "__main__":
    gearrotation()