def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    
    s.sort(key = lambda x : len(x))
    
    for i in s:
        tmp = i.split(',')
        for j in tmp :
            if int(j) not in answer :
                answer.append(int(j))
            else:
                continue
    return answer
