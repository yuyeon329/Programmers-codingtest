from collections import deque

def solution(prices):
    deq  = deque(prices)
    answer = []
    while deq :
        tmp = 0
        stock = deq.popleft()
        for i in deq :
            tmp += 1
            if i >= stock :
                continue
            else :
                break
        answer.append(tmp)
                
    return answer
