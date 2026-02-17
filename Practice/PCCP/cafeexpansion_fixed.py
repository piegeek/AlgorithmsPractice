def solution(menu, order, k):
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
        
        # Event handling - customer arrives and queue is not empty
        if t % k == 0 and (t // k) < len(order) and len(menu_queue) > 0:
            # State update
            current_waiting += 1
            
            current_menu = order[t // k]
            menu_queue.append(current_menu)
            
            # State evaluation
            pass
        
        # Event handling - customer arrives and queue is empty
        elif t % k == 0 and (t // k) < len(order) and len(menu_queue) == 0:
            # State update
            current_waiting += 1
            
            current_menu = order[t // k]
            menu_queue.append(current_menu)
            
            current_duration = 0
            
            # State evaluation
            pass
        
        current_duration += 1
        ret = max(ret, current_waiting)

    return ret