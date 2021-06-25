def solution(numbers, target):
    candidates = [0] 
        
    for i in numbers :
        tmps = []
        for j in candidates :
            tmp_plus = j + i
            tmp_minus = j - i
            tmps.append(tmp_plus)
            tmps.append(tmp_minus)
        candidates = tmps
    
    return candidates.count(target)
