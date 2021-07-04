from itertools import combinations
def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])
    candidates = []
    #모든 키의 조합 구하기
    for i in range(1, col+1):
        #range(col) : [0,1,2,3]과 동일
        candidates.extend(combinations(range(col),i))
    
    #유일성 검사   
    unique = []  
    #키를 뽑아서
    for c in candidates:
        #릴레이션의 튜플마다 각 키에 해당하는 값을 뽑아서 tuple(,,)형태로 tmp에 저장
        tmp = [tuple([item[i] for i in c]) for item in relation]
        #유일성을 만족하는지 확인 ex) (1,)같은 경우엔 동명이인이 있어 len(set(tmp)) == row가 False
        if len(set(tmp)) == row:
            unique.append(c)
    
    #최소성 검사        
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            #길이가 같으면 unique[i]의 요소와 unique[j]의 요소가 같다는 뜻이므로, unique[j]는 최소성을 만족하지 못해 삭제
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    return len(answer)
