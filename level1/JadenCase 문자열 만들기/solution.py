def solution(s):
    answer = ''
    s = s.lower()
    tmp = s.split(" ")
    
    for i in tmp :
        i = i.capitalize()
        answer += i
        answer += " "
    return answer[:-1]

print(solution(" Abc def "))
