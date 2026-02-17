def solution(menu, order, k):
    ret = 0
    
    total_duration = 0
    for i in range(len(order)):
        total_duration += menu[order[i]]
        
    queue = []
    
    end_time = 0
    duration_count = 0
    persons_waiting = 1
    order_filled = [ False for _ in range(len(order)) ]
    
    # queue.append([0, order[0]])
    
    for t in range(0, total_duration+1):
        # print(queue)
        if len(queue) >= 1:
            if duration_count == menu[queue[0][1]]:
                order_filled[queue[0][0]] = True
                duration_count = 0
                persons_waiting -= 1
                queue.pop(0)
            # else:
            #     duration_count += 1
        
        if t % k == 0:
            if all_filled(order_filled):
                break
                
            idx = (t // k)
            
            if idx <= len(order) - 1:
                queue.append([idx, order[idx]])
                persons_waiting += 1
                
        duration_count += 1
            
        ret = max(ret, len(queue))
        
    return ret

def all_filled(order_filled):
    for o in order_filled:
        if o == False:
            return False
        
    return True

def solution_new(menu, order, k):
    # State - 1. number of current customers waiting, 2. Wait queue (1 can be colllapsed into len(wait_queue)), 3. current duration, 4. menu queue
    # Events - 1. Customer arrives, 2. Menu finished
    
    current_waiting = 0
    current_duration = 0
    menu_queue = []
    
    last_time = len(order) * k
    
    # Output 
    ret = 0
    
    for t in range(0, last_time+1):
        # Event handling - menu finished
        if len(menu_queue) > 0 and current_duration == menu[menu_queue[0]]:
            # State update
            current_waiting -= 1
            menu_queue.pop(0)
            current_duration = 0
        
        # Event handling - customer arrives
        if t % k == 0 and (t // k) < len(order):
            # State update
            current_waiting += 1
            
            current_menu = order[t // k]
            menu_queue.append(current_menu)
            
            # State evaluation
            pass
        
        current_duration += 1
        ret = max(ret, current_waiting)

    return ret