def longestCommonSubsequence(str1, str2):
    n, m = len(str1), len(str2)
    
    # 2D로 변경: dp[i][j], choices[i][j]
    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    choices = [[None] * (m + 1) for _ in range(n + 1)]
    
    lcs_2(0, 0, str1, str2, dp, choices)
    
    out = []
    reconstruct_2(0, 0, str1, str2, out, choices)
    
    return out


def lcs_2(s1, s2, str1, str2, dp, choices):
    n, m = len(str1), len(str2)
    
    if s1 >= n or s2 >= m:
        return 0
    
    if dp[s1][s2] != -1:
        return dp[s1][s2]
    
    if str1[s1] == str2[s2]:
        dp[s1][s2] = 1 + lcs_2(s1 + 1, s2 + 1, str1, str2, dp, choices)
        choices[s1][s2] = ('match', s1 + 1, s2 + 1)
    else:
        skip_s1 = lcs_2(s1 + 1, s2, str1, str2, dp, choices)
        skip_s2 = lcs_2(s1, s2 + 1, str1, str2, dp, choices)
        
        if skip_s1 >= skip_s2:
            dp[s1][s2] = skip_s1
            choices[s1][s2] = ('skip', s1 + 1, s2)
        else:
            dp[s1][s2] = skip_s2
            choices[s1][s2] = ('skip', s1, s2 + 1)
    
    return dp[s1][s2]


def reconstruct_2(s1, s2, str1, str2, out, choices):
    n, m = len(str1), len(str2)
    
    if s1 >= n or s2 >= m:
        return
    
    choice = choices[s1][s2]
    if choice is None:
        return
    
    action, next_s1, next_s2 = choice
    
    if action == 'match':
        out.append(str1[s1])
    
    reconstruct_2(next_s1, next_s2, str1, str2, out, choices)


if __name__ == "__main__":
    # Test 1
    print(longestCommonSubsequence("AGGYTAB", "GXTXAYB"))  
    # ['G', 'T', 'A', 'B']
    
    # Test 2
    print(longestCommonSubsequence("clement", "antoine"))  
    # ['n', 't']
    
    # Test 3
    result = longestCommonSubsequence(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "CCCDDEGDHAGKGLWAJWKJAWGKGWJAKLGGWAFWLFFWAGJWKAG"
    )
    print(result)