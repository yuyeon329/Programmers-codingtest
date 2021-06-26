def solution(arr):
    answer = [0,0]
    length = len(arr)
    
    def compare(x,y,n):
        tmp = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != tmp:
                    n //=2
                    compare(x, y, n)
                    compare(x, y+n, n)
                    compare(x+n, y, n)
                    compare(x+n, y+n, n)
                    return
        answer[tmp] += 1 
    compare(0,0,length)
    return answer
