INF = 10 ** 9

def solution(begin, target, words):
    visited = 0
    
    ret = INF
    
    for i in range(len(words)):
        if diff_by_one(begin, words[i]):
            visited |= (1 << i)
            ret = min(ret, 1 + dfs(visited, words[i], begin, target, words))
            visited &= ~(1 << i)
    
    if ret == INF:
        return 0
    
    return ret

def dfs(visited, last, begin, target, words):
    if last == target:
        return 0
    
    ret = INF
    
    for i in range(len(words)):
        if not (visited & (1 << i)) and diff_by_one(last, words[i]):
            visited |= (1 << i)
            ret = min(ret, 1 + dfs(visited, words[i], begin, target, words))
            visited &= ~(1 << i)
            
    return ret

def diff_by_one(word1, word2):
    count_diff = 0
    
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count_diff += 1
            
    if count_diff == 1:
        return True
    else:
        return False
            