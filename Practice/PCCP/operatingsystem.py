import heapq

def solution(program):
    # Method 1
    # Event based simulation
    # Events: 1. program called 2. program operation ended
    # State: 1. queue to hold programs in line 2. Waiting time for each process 3. Total time

    # States
    queue = []
    waiting_times = [ -1 for _ in range(len(program)) ]
    total_time = 0

    # Event handling
    start = []
    for i in range(len(program)):
        start.append([i, program[i][1], program[i]])

    start = sorted(start, key = lambda x : x[1])

    i = 0
    while i < len(start):
        idx, start_time, p = start[i]
        called_together = []
        skip_idx = 1
        for j in range(idx, len(start)):
            next_idx, next_start_time, next_p = start[j]
            if next_start_time != start_time:
                break

            skip_idx += 1

            called_together.append([j, program[j]])

        for c in range(len(called_together)):
            idx, p = called_together[i]
            heapq.heappush(queue, (p[0], [idx, p]))

        i += skip_idx

    # Couldn't come up with a better solution after this

    # Method 2
    # Basically the problem can be reduced to sorting
    programs = sorted(program, key = lambda x : x[1])
    sorted_q_out = queue_sort(programs)

    print(sorted_q_out)

    end_time = 0
    end_times = [end_time]

    for item in sorted_q_out:
        start_time = item[1]
        duration = item[2]
        end_time = max(end_time, start_time + duration, end_time + duration)
        end_times.append(end_time)

    waiting = [ 0 for _ in range(11) ]

    for i in range(len(sorted_q_out)):
        score, start_time, duration = sorted_q_out[i]

        waiting[score] += end_times[i] - start_time
        

def queue_sort(program):
    sorted_queue = []
    output = []
    i = 0
    while i < len(program):
        if len(sorted_queue) > 0:
            item = sorted_queue.pop(0)
            output.append(item)

        skip_idx = 1
        sorted_queue.append(program[i])
        for j in range(i+1, len(program)):
            item_i = program[i]
            item_j = program[j]

            if item_i[1] == item_j[1]:
                skip_idx += 1
                sorted_queue.append(program[j])
            else:
                break

        sorted_queue = sorted(sorted_queue, key = lambda x : x[0])
        i += skip_idx

    while len(sorted_queue) > 0:
        output.append(sorted_queue.pop(0))

    return output