def solution(dartResult):
    answer = []
    num = ''
    
    for i in dartResult:
        if i.isnumeric() :
            num += i
            
        elif i == 'S':
            answer.append(int(num)**1)
            num = ''
            
        elif i == 'D':
            answer.append(int(num)**2)
            num = ''
            
        elif i == 'T':
            answer.append(int(num)**3)
            num = ''
            
        elif i == '#' :
            answer[-1] *= -1
            
        elif i == '*' :
            if len(answer) > 1 :
                answer[-2] *= 2
            answer[-1] *= 2
                
    return sum(answer)
