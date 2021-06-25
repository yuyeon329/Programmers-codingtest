import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while len(scoville)>1:
        if scoville[0] < K :
            tmp1 = heapq.heappop(scoville)
            tmp2 = heapq.heappop(scoville)
            heapq.heappush(scoville, tmp1+tmp2*2)
            answer += 1
        else :
            break
    if scoville[0] < K:
        answer = 0
    return -1 if answer == 0 else answer

