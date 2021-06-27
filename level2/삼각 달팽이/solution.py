def solution(n):
    tmp = [[0]*n for _ in range(n)]
    answer = []
    num = 1
    x,y = 0 , -1
    
    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0 :
                y += 1
            elif i % 3 == 1 :
                x += 1
            elif i % 3 == 2 :
                x -= 1
                y -= 1
            tmp[y][x] = num
            num+=1
    
    for i in tmp :
        for j in i : 
            if j != 0 :
                answer.append(j)
    return answer
