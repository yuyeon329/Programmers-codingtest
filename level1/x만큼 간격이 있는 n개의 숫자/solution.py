def solution(x, n):
    """
    answer = []
    for i in range(n):
        answer.append(x + x*i )
    return answer
    """
    return[x+x*i for i in range(n)]
