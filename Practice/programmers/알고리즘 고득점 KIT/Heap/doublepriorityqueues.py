# Find why this code gives incorrect results for some test cases; test cases aren't specified I get 80/100
import heapq

def solution(operations):
    left_heap = []
    right_heap = []
    median = None
    
    for i in range(len(operations)):
        op_type, operand = operations[i].split(' ')
        
        if op_type == 'I':
            num = int(operand)
            if median == None:
                median = int(operand)
            elif num <= median:
                heapq.heappush(left_heap, num)
                if len(left_heap) > len(right_heap) + 1:
                    heapq.heappush(right_heap, -median)
                    median = left_heap[-1]
                    left_heap.pop(-1)
            elif num >= median:
                heapq.heappush(right_heap, -num)
                if len(right_heap) > len(left_heap) + 1:
                    heapq.heappush(left_heap, median)
                    median = -right_heap[-1]
                    right_heap.pop(-1)
                    
        elif op_type == 'D':
            num = int(operand)
            if num == 1:
                if len(right_heap) > 0:
                    heapq.heappop(right_heap)
                else:
                    median = None
            elif num == -1:
                if len(left_heap) > 0:
                    heapq.heappop(left_heap)
                else:
                    median = None
                    
    if median != None:
        max_val = median
        if len(right_heap) > 0:
            max_val = max(max_val, -right_heap[0])
        min_val = median
        if len(left_heap) > 0:
            min_val = min(min_val, left_heap[0])
        
        return [max_val, min_val]
    else:
        if len(left_heap) > 0 and len(right_heap) > 0:
            max_val = max(left_heap)
            min_val = min(left_heap)
            max_val = max(max_val, -min(right_heap))
            min_val = min(min_val, -max(right_heap))
            return [max_val, min_val]
        elif len(left_heap) > 0:
            return [max(left_heap), min(left_heap)]
        elif len(right_heap) > 0:
            return [-min(right_heap), -max(right_heap)]
        else:
            return [0, 0]