def solution(prices):
    output = [0 for _ in range(len(prices))]
    
    for i in range(len(prices)):
        didnt_drop = True
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                didnt_drop = False
                output[i] = j - i
                break
                
        if didnt_drop:
            output[i] = len(prices) - 1 - i
            
    return output
                
        