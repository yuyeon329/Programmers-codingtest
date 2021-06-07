def solution(n):
    answer = ''
    
    while(n > 0):
        n, q = divmod(n,3)
        answer += str(q)
        
    return int(answer,3)
