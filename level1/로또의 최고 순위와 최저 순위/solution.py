def solution(lottos, win_nums):
    answer = []
    best = 0
    worst = 0
    
    for i in lottos :
        if i in win_nums:
            worst+=1
            
    num_of_zero = lottos.count(0)
    best = worst + num_of_zero
    best = 1 if best == 0 else best
    worst = 1 if worst == 0 else worst
    
    answer.append(7-best)
    answer.append(7-worst)
    
    return answer
