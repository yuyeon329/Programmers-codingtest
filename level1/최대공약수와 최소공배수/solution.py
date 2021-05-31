def GCD(a,b):
    while b > 0:
        a, b  = b, a % b
    return a

def LCM(a,b):
    return a * b / GCD(a,b)

def solution(n, m):
    answer = [GCD(n,m), LCM(n,m)]
    return answer
