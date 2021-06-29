from collections import deque

def solution(s):
    answer = 0
    paren = ["]","}",")"]
    stack = []
    stack = deque(stack)

    def check(tmp,check) :
        tmp = deque(tmp)
        for j in tmp:
            if j in ['(','{','['] :
                stack.append(j)
            else :
                if not stack :
                    return False
                pop_str = stack.pop()
                if j == ')' and pop_str != '(' :
                    return False
                elif j == '}' and pop_str != '{' :
                    return False
                elif j == ']' and pop_str != '[' :
                    return False
        return len(stack) == 0

    for i in range(-1,len(s)-1):
        tmp = s[i+1:] + s[:i+1]
        if check(tmp,stack) :
            answer += 1   
    return answer
