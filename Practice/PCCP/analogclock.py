def solution(h1, m1, s1, h2, m2, s2):
    t1 = 60 * 60 * h1 + 60 * m1 + s1
    t2 = 60 * 60 * h2 + 60 * m2 + s2
    
    alarm_rang = 0
    
    for t in range(t1, t2+1-1):
    # for t in range(t1, t1+90):
        hr_loc = get_loc_hr(t)
        mi_loc = get_loc_mi(t)
        se_loc = (6 * t) % 360
        
        if (hr_loc - (se_loc)) * (hr_loc - (se_loc+6)) <= 0:
            alarm_rang += 1
        if (mi_loc - (se_loc)) * (mi_loc - (se_loc+6)) <= 0:
            alarm_rang += 1
            
    return alarm_rang

def get_loc_hr(t):
    x = t / (60 * 60)
    y = 30 * x
    
    y_dec = y - int(y)
    
    return (int(y) % 360) + y_dec

def get_loc_mi(t):
    x = t / 60
    y = 6 * x
    
    y_dec = y - int(y)
    
    return (int(y) % 360) + y_dec
    