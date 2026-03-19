# Even in this problem - ordering of sub events are important! 
# If time for attack - successive_recovery_time resets back to 0!
def solution(bandage, health, attacks):
    # Event - get attacked

    max_health = health
    curr_health = health

    t = 0
    successive_recovery_time = 0
    attack_idx = 0

    while True:
        if attack_idx == len(attacks):
            break
       
        # Event 2 - Attacked 
        if t == attacks[attack_idx][0]:
            curr_health -= attacks[attack_idx][1]
            
            if curr_health <= 0:
                return -1

            successive_recovery_time = 0
            attack_idx += 1

        else:
            curr_health = min(max_health, curr_health+bandage[1])

        # Event 1 - Consecutive healing successful
        if successive_recovery_time == bandage[0]:
            curr_health = min(max_health, curr_health + bandage[2])
            successive_recovery_time = 0
        
        successive_recovery_time += 1
        t += 1

    return curr_health

# Previous website solutions
# def solution(bandage, health, attacks):
#     last_attack_time = attacks[-1][0]
#     curr_health = health
#     consecutive_count = 0
    
#     attack_idx = 0
    
#     for t in range(0, last_attack_time + 1):
#         # Effect? -> Shouldn't nest state evaluation and state transtion together
#         if t == attacks[attack_idx][0]:
#             # State update
#             curr_health -= attacks[attack_idx][1]
#             consecutive_count = 0
            
#             # Check invariant
#             # 1. curr_health > 0
#             if curr_health <= 0:
#                 return -1
            
#             attack_idx += 1
#         else:
#             # State update
#             curr_health += 1 * (bandage[1])
#             consecutive_count += 1
    
#             # Check invariant
#             # 1. consecutive_count < bandage[0] (x -> y; x is a transient state, y is the final state so range of y should be considered the invariant)
#             # 2. curr_health <= health
            
#             # Condition preceeds state update (is a condition of state update)
#             if consecutive_count == bandage[0]:
#                 curr_health += bandage[2]
#                 consecutive_count = 0
            
#             if curr_health > health:
#                 curr_health = health
                
#     return curr_health

def solution(bandage, health, attacks):
    t, x, y = bandage
    curr_health = health

    for i, (atk_time, damage) in enumerate(attacks):
        # 이전 공격 이후 ~ 현재 공격 직전까지의 회복 계산
        prev_time = attacks[i - 1][0] if i > 0 else 0
        gap = atk_time - prev_time - 1  # 회복 가능한 초 수

        if gap > 0:
            curr_health += gap * x + (gap // t) * y
            curr_health = min(curr_health, health)

        # 공격 적용
        curr_health -= damage
        if curr_health <= 0:
            return -1

    return curr_health
