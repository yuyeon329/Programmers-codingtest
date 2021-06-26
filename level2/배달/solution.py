from collections import deque
def solution(N, road, K):
    answer = 0
    nodes = {}
    distance = {i:float('inf') if i != 1 else 0 for i in range(1, N+1)}
    
    for v1, v2, d in road:
        nodes[v1] = nodes.get(v1, []) + [(v2, d)]
        nodes[v2] = nodes.get(v2, []) + [(v1, d)]
    que = deque([1])
    
    while que :
        current_node = que.popleft()
        for next_node, d in nodes[current_node]:
            if distance[next_node] > distance[current_node] + d :
                distance[next_node] = distance[current_node] + d
                que.append(next_node)

    
    return len([True for dist in distance.values() if dist <= K])
