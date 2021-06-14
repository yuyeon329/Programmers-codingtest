def solution(s):
    answer = ""
    
    tmp = s.split(" ")
    tmp_int = list(map(int, tmp))
    
    answer += str(min(tmp_int))
    answer += " "
    answer += str(max(tmp_int))
    
    return answer
