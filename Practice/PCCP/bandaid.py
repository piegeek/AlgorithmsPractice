def solution(bandage, health, attacks):
    # Events: 1. Attack from monster begins, 2. Attack from monster ends 3. Used heal for n consecutive seconds
    # State: 1. Current health, 2. Successive wrap time

    # Initialize states
    curr_health = health
    # wrap_time = 0
    heal_maturity = bandage[0]

    # Event simulation - Monster
    start = []

    for i in range(len(attacks)):
        start.append([attacks[i][0], -1 * attacks[i][1]])

    end = []

    for i in range(len(start) - 1):
        for j in range(1, heal_maturity):
            if start[i][0] + j <= start[-1][0]:
                if start[i][0] + j in [ x[0] for x in start ]:
                    break
                else:
                    end.append([start[i][0] + j, +1 * bandage[1]])
        # if start[i][0] + 1 not in [ x[0] for x in start ]:
        #     end.append([start[i][0] + 1, +1 * bandage[1]])

    intervals = start + end
    intervals = sorted(intervals, key = lambda x : x[0])

    # Event simulation - Heal used until maturity
    fully_healed = []
    for i in range(len(intervals) - 1):
        if intervals[i][1] > 0:
            curr_stop_time = intervals[i][0]
            fully_healed_flag = True
            for j in range(0, heal_maturity - 1):
                if curr_stop_time + j not in [ x[0] for x in intervals ]:
                    fully_healed_flag = False
                    break

            if fully_healed_flag:
                if i + heal_maturity < len(intervals):
                    next_start_time = intervals[i+heal_maturity][0]
                    if curr_stop_time + heal_maturity - 1 < next_start_time:
                        fully_healed.append([curr_stop_time + heal_maturity - 1, +1 * bandage[1] + bandage[2]])
            # next_start_time = intervals[i+1][0]
            # if curr_stop_time + heal_maturity - 1 < next_start_time:
            #     fully_healed.append([curr_stop_time + heal_maturity - 1, +1 * bandage[1] + bandage[2]])

    intervals += fully_healed
    intervals = sorted(intervals, key = lambda x : x[0])

    for event in intervals:
        time, effect = event
        print(event)
        if effect > 0:
            if curr_health + effect <= health:
                curr_health += effect
            else:
                curr_health = health
        else:
            curr_health += effect

        if curr_health <= 0:
            return -1

    return curr_health