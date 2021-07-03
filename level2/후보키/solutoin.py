from itertools import combinations
def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])
    candidates = []
    
    for i in range(1, col+1 ):
        candidates.extend(combinations(range(col),i))
    unique = []
    for c in candidates:
        tmp = [tuple([item[i] for i in c]) for item in relation]
        if len(set(tmp)) == row:
            unique.append(c)
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
            
    
    return len(answer)
