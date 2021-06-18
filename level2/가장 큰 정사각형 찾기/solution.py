def solution(board):
    max_len = 0
    if len(board)==1 and len(board[0]) == 1:
        return board[0][0]
    
    for i in range(1,len(board)):
        for j in range(1,len(board[0])): #board[1][1]부터 탐색
            if board[i][j] >=1 : 
                board[i][j] = min(board[i-1][j-1],board[i-1][j],board[i][j-1])+1
                
                if board[i][j] > max_len:
                    max_len = board[i][j]
    
    return max_len**2
