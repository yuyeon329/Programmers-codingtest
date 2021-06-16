def solution(n):

    a = format(n, 'b')
    cnt_a = list(a).count('1')
        
    while True:
        n +=1
        b = format(n, 'b')
        cnt_b = list(b).count('1')
        
        if cnt_a == cnt_b :
            break
        
    return n
