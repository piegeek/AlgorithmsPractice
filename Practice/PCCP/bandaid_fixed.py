# Time step state transition simulation blueprint
def solution(bandage, health, attacks):
    last_attack_time = attacks[-1][0]
    curr_health = health
    consecutive_count = 0
    
    attack_idx = 0
    
    for t in range(0, last_attack_time + 1):
		# Event detection
        if t == attacks[attack_idx][0]:
            # State update (State transition)
            curr_health -= attacks[attack_idx][1]
            consecutive_count = 0
            
            # Check invariant (State evaluation)
            # 1. curr_health > 0
            if curr_health <= 0:
                return -1
            
            attack_idx += 1
        else:
            # State update (State transition)
            curr_health += 1 * (bandage[1])
            consecutive_count += 1
    
            # Check invariant (State evaluation)
            # 1. consecutive_count < bandage[0] (x -> y; x is a transient state, y is the final state so range of y should be considered the invariant)
            # 2. curr_health <= health
            
            # Condition preceeds state update (is a condition of state update)
            if consecutive_count == bandage[0]:
                curr_health += bandage[2]
                consecutive_count = 0
            
            if curr_health > health:
                curr_health = health
                
    return curr_health
                
                
            