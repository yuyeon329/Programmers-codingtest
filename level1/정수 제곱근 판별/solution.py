def solution(n):
    return -1 if n **(1/2) % 1 else (n **(1/2) + 1 ) **2
