def l_distance(s1, s2):
    from functools import lru_cache

    @lru_cache(None)
    def dp(i, j):
        # If s1 exhausted, insert remaining s2 chars
        if i == len(s1):
            return len(s2) - j
        
        # If s2 exhausted, delete remaining s1 chars
        if j == len(s2):
            return len(s1) - i
        
        # If characters match, move both
        if s1[i] == s2[j]:
            return dp(i + 1, j + 1)
        
        # Otherwise try all 3 operations
        return 1 + min(
            dp(i + 1, j + 1),  # Replace
            dp(i + 1, j),      # Delete from s1
            dp(i, j + 1)       # Insert into s1
        )
    
    return dp(0, 0)