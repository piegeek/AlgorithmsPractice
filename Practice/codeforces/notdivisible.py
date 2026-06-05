def notdivisible():
    C, test_cases = parse_input()

    for i in range(C):
        n, k = test_cases[i]
        print(solve_notdivisible(n, k))

def solve_notdivisible(n, k):
    lo = 0
    hi = 10 ** 9

    mid = (lo + hi) // 2

    count = 0

    while count != k:
        # print([count, k])
        
        count = mid - (mid // n)
        
        if count < k:
            lo = mid
        else:
            hi = mid
        
        mid = (lo + hi) // 2 

    return mid

    # count = 0
    # x = 0

    # while count < k:
    # 	if x % n != 0:
    # 		count += 1

    # 	if count == k:
    # 		break

    # 	x += 1

    # return x


def parse_input():
    C = int(input())

    test_cases = []

    for _ in range(C):
        n, k = tuple(map(int, input().split()))

        test_cases.append([n, k])

    return C, test_cases


if __name__ == '__main__':
    notdivisible()