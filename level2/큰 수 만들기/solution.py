def solution(number, k):
    stack = []
    for i in number:
        while stack and stack[-1] < i and k > 0 :
            stack.pop()
            k -= 1
        stack.append(i)           
        
    return "".join(stack[:len(stack)-k])
