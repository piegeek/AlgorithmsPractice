import sys
import heapq

def editdistance():
    s1, s2 = parse_input()
    solve_editdistance(s1, s2)

def solve_editdistance(s1, s2):
    # Sol 1
    # visited = [ False for _ in range(len(s1)) ]

    # equals = []

    # for i in range(len(s1)):
    #     for j in range(len(s2)):
    #         if s1[i] == s2[j] and visited[i] == False:
    #             k = 0

    #             while i+k < len(s1) and j+k < len(s2) and s1[i+k] == s2[j+k]:
    #                 visited[i+k] = True
    #                 k += 1

    #             equals.append(s1[i:i+k])

    # print(equals)

    # equals_len = sum([len(x) for x in equals])
    # ret = max(len(s1) - equals_len, len(s2) - equals_len)

    # print(ret)
    # return ret
    
    # Sol 2 - BFS
    # shorter = s1 if len(s1) < len(s2) else s2
    # longer  = s2 if len(s1) < len(s2) else s1

    # count = 0

    # queue = []

    # heapq.heappush(queue, (count, shorter))

    # while len(queue) > 0:
    #     count, string = heapq.heappop(queue)

    #     if string == longer:
    #         return count

    #     for char in longer:
    #         if char not in string:
    #             pass

    # Sol 3
    ret = l_distance(0, 0, s1, s2)
    print(ret)
    return ret

# Since this has to be memoized (look at input size), s1, s2 shouldn't be modified
def l_distance(a, b, s1, s2):
    if a == len(s1) or b == len(s2):
        return 0
    
    if s1[a] == s2[b]:
        return l_distance(a + 1, b + 1, s1, s2)
    else:
        return min(
            1 + l_distance(a + 1, b + 1, s1, s2), # Replacement
            1 + l_distance(a + 1, b + 1, s1[:a] + s2[b] + s1[a:], s2), # Insertion to s1
            1 + l_distance(a + 1, b + 1, s1, s2[:b] + s1[a] + s2[b:])  # Insertion to s2
        )

def parse_input():
    input = sys.stdin.readline
    
    s1 = input().strip()
    s2 = input().strip()
    
    return s1, s2


if __name__ == "__main__":
    editdistance()