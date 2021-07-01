from collections import deque
def solution(maps):
    w = len(maps[0]) #리스트의 가로
    h = len(maps) #리스트의 세로
     
    #동서남북으로 이동하기 위한 좌표
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    #첫번째 시작하는 좌표인 0,0
    queue = deque([[0,0]])
    
    #끝에 도달할 때까지 while문 반복
    while len(queue)  != 0 :
        #직전 위치의 좌표 x,y
        x,y = queue.popleft()
        #새로운 칸으로 가기 위해 4방향으로 모두 탐색 (bfs)
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            
            #탐색한 위치가 맵의 크기에 유효하고, 가본적이 없는 곳이라면
            if 0<=cx<h and 0<=cy<w and maps[cx][cy] == 1:
                #큐에 추가함으로써 다음 이동때 직전 위치로 사용
                queue.append([cx,cy])
                #맵에 방문 표시 (이제까지 지나온 칸의 갯수)
                maps[cx][cy] = maps[x][y] + 1
    #끝까지 가지 못했다면 못가는 진영이므로 -1 아니면 끝까지 도착할때까지 지나온 칸의 갯수 출력   
    return -1 if maps[-1][-1] == 1 else maps[h-1][w-1]
