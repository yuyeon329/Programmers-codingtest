"""
def solution(s):
    answer = ''
    tmp = []

    for i in s:
        tmp.append(ord(i))
    tmp = sorted(tmp, reverse = True)
    
    for i in tmp:
        answer+= chr(i)
    return answer
    """
def solution(s):
    return "".join(sorted(s, reverse=True))
