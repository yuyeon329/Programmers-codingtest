def solution(n):
    answer = ''
    
    while (n>0):
        n, q = divmod(n,3)
        if q == 0:
            n , q = n-1, 4 
        answer = str(q) + answer
    return answer
