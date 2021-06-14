def solution(n):
    return fib(n) % 1234567

def fib(n):
    list_num = [0,1]
    for i in range(n-1):
        list_num.append(list_num[-1]+list_num[-2])
    
    return list_num[-1]
