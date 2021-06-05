def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    return sorted(answer) if len(answer) > 0 else [-1]
"""
def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]
"""
