def solution(new_id):
    answer = ''
    
    #1단계
    tmp = new_id.lower()

    #2단계
    for word in tmp:
        if word.isalnum() or word in '-_.':
            answer += word

    #3단계
    while '..' in answer:
        answer = answer.replace('..','.')
        
    #4단계
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer 
    
    #5단계
    answer = "a" if answer == "" else answer
    
    #6단계
    answer = answer[0:15] if len(answer) >15 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    
    #7단계
    if len(answer) < 3 : 
        answer += answer[-1] * (3 - len(answer))
    
    return answer
