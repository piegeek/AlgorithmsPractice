import sys

def meetingroom():
    test_cases = parse_input()

    for i, (N, teams) in enumerate(test_cases, 1):
        solve_meetingroom(N, teams)

def solve_meetingroom(N, teams):
    ret = dp(0, -1, N, teams)
    answers = reconstruct(0, -1, N, teams)

    print(ret)
    print(answers)

def dp(idx, last, N, teams):
    # 끝까지 배정을 완료했다 - 성공이므로 True return
    if idx == N:
        return True

    ret1 = False
    ret2 = False

    # Yes week
    if teams[idx][0] >= last:
        ret1 = dp(idx+1, teams[idx][1], N, teams)

    # Yes month
    if teams[idx][2] >= last:
        ret2 = dp(idx+1, teams[idx][3], N, teams)

    return ret1 or ret2

# Reconstruct
# 0. Base case - [[]] or []
# 1. Set current_val
# 2. Compare current_val to next step
# 3. suffixes = reconstruct(...)
# 4. When appending answers be mindful of the order format of answer
# 5. Be aware of typos
def reconstruct(idx, last, N, teams):
    if idx == N:
        return [[]]

    current_val = dp(idx, last, N, teams)

    answers = []

    # Yes week
    if teams[idx][0] >= last:
        if current_val == dp(idx+1, teams[idx][1], N, teams):
        # if dp(idx+1, teams[idx][1], N, teams) == True:
            suffixes = reconstruct(idx+1, teams[idx][1], N, teams)
            for suf in suffixes:
                answers.append([[teams[idx][0], teams[idx][1]]] + suf)

    # Yes month
    if teams[idx][2] >= last:
        if current_val == dp(idx+1, teams[idx][3], N, teams):
        # if dp(idx+1, teams[idx][3], N, teams) == True:
            # BE AWARE OF TYPOS
            suffixes = reconstruct(idx+1, teams[idx][3], N, teams)
            for suf in suffixes:
                answers.append([[teams[idx][2], teams[idx][3]]] + suf)

    return answers

def parse_input():
    input = sys.stdin.readline
    
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        N = int(input().strip())
        
        teams = []
        for _ in range(N):
            a, b, c, d = map(int, input().split())
            teams.append((a, b, c, d))
        
        test_cases.append((N, teams))

    return test_cases


# Example usage
if __name__ == "__main__":
    meetingroom()