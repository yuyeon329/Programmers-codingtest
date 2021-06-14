def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)) :
        tmp_l = []
        for j in range(len(arr2[0])):
            tmp = 0
            for k in range(len(arr1[0])):
                tmp += arr1[i][k] * arr2[k][j]
            tmp_l.append(tmp)
        answer.append(tmp_l)
    
    return answer
