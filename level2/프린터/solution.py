from collections import deque

def solution(priorities, location):
    answer = 0
    deq = deque([(j,i) for i,j in enumerate(priorities)])

    while len(deq):
        tmp = deq.popleft()
        if deq and max(deq)[0] > tmp[0]:
            deq.append(tmp)
        else:
            answer += 1
            if tmp[1] == location :
                break
    return answer
