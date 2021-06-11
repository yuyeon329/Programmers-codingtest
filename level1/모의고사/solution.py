def solution(answers):
    count = [0,0,0]
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    answers_len = len(answers)
    
    for i in range(answers_len):
        if a[i%5] == answers[i]:
            count[0] += 1
        if b[i%8] == answers[i]:
            count[1] += 1
        if c[i%10] == answers[i]:
            count[2] += 1    
        
    for i in range(3):
        if count[i] == max(count):
            answer.append(i+1)
            
    return answer
