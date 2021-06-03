def solution(s, n):
    my_str = list(s)
    answer = ''
    for i in my_str:
        if i.isupper() :
            answer += chr((ord(i)-ord('A')+n) % 26 + ord('A'))
            
        elif i.islower() :
            answer += chr((ord(i)-ord('a')+n) % 26 + ord('a'))
            
        else:
            answer += i
            
    return answer
