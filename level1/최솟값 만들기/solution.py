def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse = True)
    
    for i,j in zip(A, B):
        answer += i * j


    return answer
