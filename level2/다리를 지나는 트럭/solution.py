from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    my_queue = [0]*bridge_length

    while my_queue:
        time += 1
        my_queue.pop(0)
        if truck_weights:
            if sum(my_queue) + truck_weights[0] <= weight :
                my_queue.append(truck_weights.pop(0))
            else :
                my_queue.append(0)
                
    return time

