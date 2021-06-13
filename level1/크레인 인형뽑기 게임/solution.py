def solution(board, moves):
    answer = 0
    basket = []

    for i in moves:
        for j in range(len(board[0])):
            tmp = board[j][i-1]
            
            if tmp != 0:
                basket.append(tmp)
                board[j][i-1] = 0
                
                if len(basket) > 1 :
                    if basket[-2] == tmp :
                        basket.pop()
                        basket.pop()
                        answer +=1
                break
