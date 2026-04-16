import heapq
import copy

def solution(name):
    start = ['A'] * len(name)
    
    alphabet = [chr(x).upper() for x in range(97, 97+26)]
    
    cursor = 0
    
    ret = 0
    
    while ''.join(start) != name:
        if start[cursor] != name[cursor]:
            alphabet_idx = alphabet.index(name[cursor])
            ret += min((26 - alphabet_idx), alphabet_idx)
            start[cursor] = name[cursor]
        
        right_idx = None
        left_idx = None
        
        # Search right of cursor
        for i in range(len(name)):
            idx = (cursor + i) % len(name)
            if start[idx] != name[idx]:
                right_idx = idx
                break
                
        # Search left of cursor     
        for i in range(len(name)):
            idx = (cursor - i) % len(name)
            if start[idx] != name[idx]:
                left_idx = idx
                break

        if right_idx == None and left_idx == None:
            break

        if right_idx == None:
            while cursor != left_idx:
                cursor = (cursor - 1) % len(name)
                ret += 1
            
        elif left_idx == None:
            while cursor != right_idx:  
                cursor = (cursor + 1) % len(name)
                ret += 1
                
        elif right_idx != None and left_idx != None:
            if (cursor - left_idx) % len(name) <= (right_idx - cursor) % len(name):
                ret += (cursor - left_idx) % len(name)
                cursor = left_idx
            else:
                ret += (right_idx - cursor) % len(name)
                cursor = right_idx
                
    return ret
            

def solution_bfs(name):
    start = 'A' * len(name)
    
    queue = []
    
    alphabet = [chr(x).upper() for x in range(97, 97+26)]
    
    heapq.heappush(queue, (0, [0, start]))
    
    while len(queue) > 0:
        step, item = heapq.heappop(queue)
        
        cursor, string = item
        
        if string == name:
            return step
        
        curr_alphabet = string[cursor]
        curr_alphabet_idx = alphabet.index(curr_alphabet)
        
        next_alphabet = alphabet[(curr_alphabet_idx + 1) % 26]
        string_copy_list = list(copy.deepcopy(string))
        string_copy_list[cursor] = next_alphabet
        string_copy = ''.join(string_copy_list)
        heapq.heappush(queue, (step + 1, [cursor, string_copy]))
        
        prev_alphabet = alphabet[(curr_alphabet_idx - 1) % 26]
        string_copy_list = list(copy.deepcopy(string))
        string_copy_list[cursor] = prev_alphabet
        string_copy = ''.join(string_copy_list)
        heapq.heappush(queue, (step + 1, [cursor, string_copy]))
        
        # Move cursor to the left
        heapq.heappush(queue, (step + 1, [(cursor - 1) % len(name), string]))
        
        # Move cursor to the right
        heapq.heappush(queue, (step + 1, [(cursor + 1) % len(name), string]))
        
    
if __name__ == '__main__':
    print(solution('JAN'))
    