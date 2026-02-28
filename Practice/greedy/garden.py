# BOJ 2457
import sys

INF = 10 ** 9

def garden():
    N, flowers = parse_input()
    solve_garden(N, flowers)

def solve_garden(N, flowers):
    flowers = sorted(flowers, key = lambda x : (x[0], x[1]))

    start = INF
    end = 0

    ret = dp(0, start, end, N, flowers, True)
    print(ret)

    answers = reconstruct(0, start, end, N, flowers, True)
    print(answers)
    return ret

    # count = greedy(N, flowers)
    # print(count)
    # return count

def greedy(N, flowers):
    count = 0
    end_time = 3.01
    
    idx = 0

    while end_time <= 11.30:
        max_end = end_time
        while idx < N and flowers[idx][0] <= end_time:
            max_end = max(max_end, flowers[idx][1])
            idx += 1

        if max_end == end_time:
            return 0

        count += 1
        end_time = max_end

    return count

def greedy_GPT(N, flowers):
    # Convert dates first if needed
    # flowers.sort(key=lambda x: (x[0], x[1]))

    idx = 0
    count = 0
    end_time = 3.01

    while end_time <= 11.30:
        max_end = end_time

        while idx < N and flowers[idx][0] <= end_time:
            max_end = max(max_end, flowers[idx][1])
            idx += 1

        # Cannot extend coverage
        if max_end == end_time:
            return 0

        end_time = max_end
        count += 1

    return count

def dp(idx, start, end, N, flowers, empty):
    if idx == N:
        if end >= 11.30 and start <= 3.01:
            print(f'end: {end}, start: {start}')
            return 0
        else:
            return INF

    # Skip idx
    ret = dp(idx + 1, start, end, N, flowers, empty)

    # Take idx - Empty
    if empty == True:
        start = min(start, flowers[idx][0])
        end = max(end, flowers[idx][1])
        ret = min(ret, 1 + dp(idx + 1, start, end, N, flowers, False))
        return ret

    # Take idx
    # Feasibility check
    if flowers[idx][0] <= end:
        # Merge intervals
        start = min(start, flowers[idx][0])
        end = max(end, flowers[idx][1])
        ret = min(ret, 1 + dp(idx + 1, start, end, N, flowers, False))

    return ret

def reconstruct(idx, start, end, N, flowers, empty):
    if idx == N:
        if end >= 11.30 and start <= 3.01:
            return [[]]
        # For this case we returned INF in dp() here we return []
        else:
            return []

    current_val = dp(idx, start, end, N, flowers, empty)
    
    answers = []

    if current_val == dp(idx + 1, start, end, N, flowers, empty):
        # Should include answer for skip except dont add flowers[idx] into the answer
        suffixes = reconstruct(idx + 1, start, end, N, flowers, empty)
        for suf in suffixes:
            answers.append(suf)

    # Take idx - Empty
    if empty == True:
        start = min(start, flowers[idx][0])
        end = max(end, flowers[idx][1])
        if current_val == 1 + dp(idx + 1, start, end, N, flowers, False):
            suffixes = reconstruct(idx + 1, start, end, N, flowers, False)
            # Put [flowers[idx]] first
            for suf in suffixes:
                answers.append([flowers[idx]] + suf)
            
            return answers
    
    # Take idx
    # Feasibility check
    # Greedy key - choose max end
    if flowers[idx][0] <= end:
        # Merge intervals
        start = min(start, flowers[idx][0])
        end = max(end, flowers[idx][1])
        if current_val == 1 + dp(idx + 1, start, end, N, flowers, False):
            suffixes = reconstruct(idx + 1, start, end, N, flowers, False)
            # Put [flowers[idx]] first
            for suf in suffixes:
                answers.append([flowers[idx]] + suf)

    return answers
            

def parse_input():
    input = sys.stdin.readline  # fast input
    
    N = int(input().strip())
    
    flowers = []
    flowers_decimal = []
    for _ in range(N):
        start_month, start_day, end_month, end_day = map(str, input().split())
        flowers.append((start_month, start_day, end_month, end_day))

        padded_start_day = '0' + start_day if len(start_day) == 1 else start_day
        padded_end_day = '0' + end_day if len(end_day) == 1 else end_day


        flowers_decimal.append((float(start_month + '.' + padded_start_day), float(end_month + '.' + padded_end_day)))
    
    return N, flowers_decimal


# Example usage
if __name__ == "__main__":
    garden()