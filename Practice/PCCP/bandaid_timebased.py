def solution(bandage, health, attacks):
    last_attack_time = attacks[-1][0]
    attack_times = [ x[0] for x in attacks ]
    
    curr_health = health
    
    heal_count = 0
    
    attack = False
    
    for t in range(1, last_attack_time + 1):
        # Doesn't return immediately after attack; Returns at next second
        # if curr_health <= 0:
        #     return -1
        
        if t in attack_times:
            heal_count = 0
            attack = True
            attack_damage = attacks[attack_times.index(t)][1]
            curr_health -= attack_damage

            if curr_health <= 0:
                return -1
        else:
            attack = False
            heal_count += 1
            # if curr_health < health:
            #     if heal_count < bandage[0]:
            #         curr_health += bandage[1]

            curr_health = min(health, curr_health + bandage[1])

            if heal_count == bandage[0]:
                # if curr_health + bandage[1] + bandage[2] <= health:
                #     curr_health += bandage[1]
                #     curr_health += bandage[2]
                # else:
                #     curr_health = health
                # heal_count = 0
                # continue
                curr_health = min(health, curr_health + bandage[2])
                heal_count -= 1
            
        print(f'curr_health: {curr_health}, heal_count: {heal_count}, attack: {attack}')
            
    
    if curr_health <= 0:
        ret = -1
    elif curr_health > 0:
        ret = curr_health
    
    return ret