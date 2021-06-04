def solution(n):
    answer = 0
    prime =  [False] * 2 + [True] * (n - 1)
    
    i = int(n ** .5)
    for j in range(2, i +1):
        if prime[j] == True:
            for k in range(j+j, n + 1, j):
                prime[k] = False
                 
    for m in prime:
        if m == True :
            answer += 1
            
    return answer
