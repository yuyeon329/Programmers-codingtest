def solution(s):
    my_stack = []
    
    for i in s:
        if i == ")" and my_stack:
            my_stack.pop()
        else:
            my_stack.append(i)

    return True if not my_stack else False
