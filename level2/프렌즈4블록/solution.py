def solution(m, n, board):
    answer = 0
    #board를 리스트로 바꿔주기
    for i in range(len(board)):
        board[i] = list(board[i])
    while True: #블록을 지울 수 있을 때까지 계속 실행된다.
        #board와 같은 크기의 remove선언 후, 모양이 같은 2x2블럭의 위치를  remove에 1로 표시한다.
        remove = [[0]*n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1): #2x2블록의 중첩 가능
                #블록이 존재하고 2x2블록의 모양이 같으면
                if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove[i][j], remove[i][j+1], remove[i+1][j], remove[i+1][j+1] = 1,1,1,1
        count = 0
        
        #remove를 순회하며 지워진 블록 갯수 세기
        for i in range(m):
            count += sum(remove[i])
        answer += count    
        
        #만약 지워진 블록이 없다면 break 
        if count == 0:
            break
        
        #지워진 블록으로 인해 빈 공간 채우기
        """
        좌하단부터 탐색하며 2x2가 1인 경우에 블록을 땡겨준다. 
        여기서 처음 지워줄 경우엔 위에 있는 블록이 아래로 떨어지는 것이고, 
        블록이 떨어지고 난 후 빈 블록칸을 1과 0을 이용해 표시한다.
        아래의 For문이 블록이 떨어지는 상황 자체를 표현한 것이다.
        """
        for i in range(m-1, -1, -1):
            for j in range(n): #좌하단부터 탐색
                if  remove[i][j] == 1: #만약 1이면
                    x = i - 1 
                    while x >= 0 and remove[x][j] == 1: 
                        x -=1 
                    if x < 0 :
                        board[i][j] = 0 
                    else :
                        board[i][j] = board[x][j] 
                        remove[x][j] = 1    
    return answer
