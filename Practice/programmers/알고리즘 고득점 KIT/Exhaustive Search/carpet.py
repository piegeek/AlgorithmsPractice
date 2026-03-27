def solution(brown, yellow):
    # w >= h
    sum = (brown - 4) / 2
    mult = yellow
    
    w = (sum + ((sum) ** 2 - 4 * mult) ** (1/2)) / 2
    h = (sum - ((sum) ** 2 - 4 * mult) ** (1/2)) / 2
    
    return [w+2, h+2]