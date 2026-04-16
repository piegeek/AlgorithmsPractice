import sys
import itertools

INF = 10 ** 9

sys.setrecursionlimit(10 ** 6)

def solution(people, limit):
    visited = 0
    
    ret = INF
    
    cache = {}
    
    for i in range(len(people)):
        visited |= (1 << i)
        ret = min(ret, dfs(visited, people[i], people, limit, cache))
        visited &= ~(1 << i)
        
    return ret

def dfs(visited, curr_cap, people, limit, cache):
    ret = INF
    
    if (visited, curr_cap) in cache: return cache[(visited, curr_cap)]
    
    if visited == (1 << len(people)) - 1:
        return 1
    
    for i in range(len(people)):
        if not (visited & (1 << i)):
            if curr_cap + people[i] <= limit:
                visited |= (1 << i)
                ret = min(ret, dfs(visited, curr_cap + people[i], people, limit, cache))
                visited &= ~(1 << i)
            elif curr_cap + people[i] > limit:
                visited |= (1 << i)
                ret = min(ret, 1 + dfs(visited, people[i], people, limit, cache))
                visited &= ~(1 << i)
               
    cache[(visited, curr_cap)] = ret
    return ret
        

def solution_greedy(people, limit):
    S = []

    E = []

    indices = [i for i in range(len(people))]

    combs = itertools.combinations(indices, 2)

    for comb in combs:
        i, j = comb
        if people[i] + people[j] <= limit:
            E.append([people[i] + people[j], i, j])

    E = sorted(E, key = lambda x : x[0], reverse = True)

    for e in E:
        if is_independent(S, e, people, limit):
            S.append(e)

    paired = len(S)
    unpaired = len(people) - 2 * paired
    return len(S) + unpaired

def is_independent(S, e, people, limit):
    curr_people = [x[1] for x in S] + [x[2] for x in S]
    curr_people = set(curr_people)

    if e[1] in curr_people or e[2] in curr_people:
        return False
    else:
        return True