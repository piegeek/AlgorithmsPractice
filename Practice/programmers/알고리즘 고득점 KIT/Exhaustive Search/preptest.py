# Produces incorrect results for some inputs...
def solution(answers):
    # Simulate 1
    sim_1 = []
    i = 1
    
    while len(sim_1) < len(answers):
        sim_1.append(i)
        i += 1
        
        if i > 5:
            i = 1
            
    # Simulate 2
    sim_2 = []
    i = 0
    
    while len(sim_2) < len(answers):
        if i % 2 == 0:
            sim_2.append(2)
        else:
            if ((i - 1) / 2) % 4 == 0:
                sim_2.append(1)
            if ((i - 1) / 2) % 4 == 1:
                sim_2.append(3)
            if ((i - 1) / 2) % 4 == 2:
                sim_2.append(5)
            if ((i - 1) / 2) % 4 == 3:
                sim_2.append(7)
        i += 1
            
    # Simulate 3
    sim_3 = []
    i = 0
    
    while len(sim_3) < len(answers):
        if i % 10 in [0, 1]:
            sim_3.append(3)
        if i % 10 in [2, 3]:
            sim_3.append(1)
        if i % 10 in [4, 5]:
            sim_3.append(2)
        if i % 10 in [6, 7]:
            sim_3.append(4)
        if i % 10 in [8, 9]:
            sim_3.append(5)
            
        i += 1
    
    # print(sim_1)
    # print(sim_2)
    # print(sim_3)
    
    scores = [0 for _ in range(3)]
    
    for i in range(len(answers)):
        if sim_1[i] == answers[i]:
            scores[1-1] += 1
        if sim_2[i] == answers[i]:
            scores[2-1] += 1
        if sim_3[i] == answers[i]:
            scores[3-1] += 1
            
    max_score = max(scores)
    
    got_max_score = [x+1 for x in range(3) if scores[x] == max_score]
    return got_max_score
        
    