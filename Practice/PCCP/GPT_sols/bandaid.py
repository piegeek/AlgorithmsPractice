def solution(bandage, health, attacks):
    last_attack_time = attacks[-1][0]
    
    curr_health = health
    heal_count = 0
    
    attack_idx = 0  # instead of attack_times + index()
    
    for t in range(1, last_attack_time + 1):
        
        # Check attack
        if attack_idx < len(attacks) and t == attacks[attack_idx][0]:
            heal_count = 0
            curr_health -= attacks[attack_idx][1]
            attack_idx += 1
            
            if curr_health <= 0:
                return -1
        
        # Healing phase
        else:
            heal_count += 1
            
            # Always apply per-second heal (cap with min)
            curr_health = min(health, curr_health + bandage[1])
            
            # Always check maturity independently of health
            if heal_count == bandage[0]:
                curr_health = min(health, curr_health + bandage[2])
                heal_count = 0
        
        print(f'curr_health: {curr_health}, heal_count: {heal_count}')
    
    return curr_health
