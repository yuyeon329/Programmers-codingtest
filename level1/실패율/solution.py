def solution(N, stages):
    tmp = {}
    user = len(stages)
    
    for i in range(1, N + 1):
        if user != 0 :
            count  = stages.count(i)
            tmp[i] = count/user
            user -= count
        else :
            tmp[i] = 0
    
    return sorted(tmp, key = lambda x : tmp[x], reverse = True)
