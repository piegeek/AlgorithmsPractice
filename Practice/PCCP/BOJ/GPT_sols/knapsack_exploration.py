from functools import lru_cache

def knapsack_exploration(weights, values, capacity):
    n = len(weights)

    @lru_cache(None)
    def dp(mask, W):
        best = 0
        
        for i in range(n):
            # if item i not used yet
            if not (mask & (1 << i)):
                if weights[i] <= W:
                    candidate = values[i] + dp(mask | (1 << i),
                                               W - weights[i])
                    best = max(best, candidate)
        
        return best

    return dp(0, capacity)
