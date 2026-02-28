def greedy(N, K, heights):
    heights.sort()
    
    gaps = []
    for i in range(N - 1):
        gaps.append(heights[i+1] - heights[i])
    
    gaps.sort(reverse=True)
    
    total_span = heights[-1] - heights[0]
    
    return total_span - sum(gaps[:K-1])