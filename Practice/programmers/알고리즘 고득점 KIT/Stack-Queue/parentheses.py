# Why my dp solution doesn't work here... how to make it work
def solution(s):
    left = 0
    right = len(s) - 1
    
    ret = dp(left, right, s)
    
    return ret

def dp(left, right, s):
    if right - left == 1:
        if s[left] == '(' and s[right] == ')':
            return True
        
    ret = False
    
    for i in range(left + 1, right):
        ret = ret or (dp(left, i, s) and dp(i+1, right, s))
        
    return ret

# Stack sol
def solution(s):
    stack = []
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop(-1)
            else:
                stack.append(s[i])
                
    return len(stack) == 0