def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
    c.append("")
    
    for i in range(len(p)):
        if p[i] != c[i]:
            return p[i]
