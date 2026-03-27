def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    stack = []
    count = [0]
    word_found = False
    
    for v in vowels:
        stack.append(v)
        if dfs(word, vowels, stack, count, 1):
            word_found = True
        stack.pop(-1)
        
        if word_found == True:
            break
            
    return count[0]
    
    
def dfs(word, vowels, stack, count, level):
    count[0] += 1

    if word == ''.join(stack):
        return True
    
    word_found = False
    
    for v in vowels:
        if level+1 <= 5:
            stack.append(v)
            if dfs(word, vowels, stack, count, level+1):
                word_found = True
            stack.pop(-1)
            
        if word_found == True:
            return True
        
    return False