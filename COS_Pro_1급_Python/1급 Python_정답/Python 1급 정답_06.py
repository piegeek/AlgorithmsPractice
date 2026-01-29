def solution(start, locations):
    answer = 0
    min = 100 #here
    max = 0
    for i in locations:
        if i < min:
            min = i
        if i > max:
            max = i
            
    if start <= min:
        answer = max - start
    elif start >= max:
        answer = start - min
    else:
        if start - min < max - start:
            answer = start - min + (max - min)
        else:
            answer = max - start + (max - min)
            
    return answer