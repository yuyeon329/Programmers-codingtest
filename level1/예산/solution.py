def solution(d, budget):
    answer = 0
    d = sorted(d)
    
    for i in range(len(d)) :
        tmp = sum(d[:i+1])
        if tmp <= budget:
            answer = i + 1
            
    return answer
