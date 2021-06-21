def solution(brown, yellow):
    for i in range(1,yellow+1):
        if yellow % i == 0:
            j = yellow // i
            if (i + 2) * (j + 2) - (i * j) == brown:
                return [max(i,j)+2, min(i,j)+2]
            else:
                continue
        else: continue
            
            
            
