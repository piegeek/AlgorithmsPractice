def solution(video_len, pos, op_start, op_end, commands):
    video_len_int, pos_int, op_start_int, op_end_int = list(map(time_to_int, [video_len, pos, op_start, op_end]))
    
    curr = pos_int
    
    for command in commands:
        if op_start_int <= curr and curr <= op_end_int:
            curr = op_end_int
        
        if command == 'next':
            curr = min(curr+10, video_len_int)
            
        elif command == 'prev':
            curr = max(curr-10, 0)
            
    if op_start_int <= curr and curr <= op_end_int:
        curr = op_end_int        
            
    return int_to_time(curr)
    
    
def time_to_int(time):
    time_list = list(map(int, time.split(':')))
    
    return 60 * time_list[0] + time_list[1]

def int_to_time(time_int):
    hour = time_int // 60
    minute = time_int % 60
    
    hour_str = str(hour)
    minute_str = str(minute)
    
    if len(hour_str) == 1:
        hour_str = '0' + hour_str
        
    if len(minute_str) == 1:
        minute_str = '0' + minute_str
    
    return ':'.join([hour_str, minute_str])