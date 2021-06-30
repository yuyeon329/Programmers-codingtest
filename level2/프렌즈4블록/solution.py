def solution(m, n, board):
    board = list(map(list, zip(*board)))
    
    def game(b):
        pops = 0
        sc = [i[:] for i in b]
        for i in range(n-1):
            for j in range(m-1):
                if b[i][j] == -1: continue
                if b[i][j] == b[i+1][j] == b[i+1][j+1] == b[i][j+1]:
                    sc[i][j], sc[i+1][j], sc[i+1][j+1], sc[i][j+1] = 0,0,0,0
        
        for i,v in enumerate(sc):
            cnt = v.count(0)
            pops += cnt
            sc[i] =[-1]*cnt + [a for a in v if a!=0]
        
        return sc, pops
    
    answer = 0
    
    while True:
        board, pops = game(board)
        
        if pops == 0:  return answer
        
        answer += pops
