def solution(n, t, m, p):
    answer = ''
    alpha = ['A', 'B', 'C', 'D', 'E', 'F']
    cnt = 0
    result = '0'

    while len(answer) < t:
        r = cnt
        tmp_len2 = ''
        while r > 0 :
            r, q = divmod(r, n)
            if q > 9 :
                tmp_len2 = alpha[q-10] + tmp_len2
            else:
                tmp_len2 = str(q) + tmp_len2
        cnt += 1
        result += tmp_len2
        answer = ''

        for i in range(p-1,len(result)-1,m):
            answer += result[i]
        
    return answer
