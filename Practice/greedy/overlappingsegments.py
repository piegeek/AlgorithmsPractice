# BOJ 1689
import sys
import heapq

def overlappingsegments():
    N, segments = parse_input()
    solve_overlappingsegments(N, segments)

def solve_overlappingsegments(N, segments):
    segments = sorted(segments, key = lambda x : x[0])

    heap = []

    ret = 0

    for seg in segments:
        if len(heap) > 0 and seg[0] > heap[0][0]:
            heap = []

        else:
            heapq.heappush(heap, (seg[1], seg))

        ret = max(ret, len(heap))

    print(ret)
    return ret


def parse_input():
    input = sys.stdin.readline  # fast input
    
    N = int(input().strip())
    
    segments = []
    for _ in range(N):
        s, e = map(int, input().split())
        segments.append((s, e))
    
    return N, segments


# Example usage
if __name__ == "__main__":
    overlappingsegments()