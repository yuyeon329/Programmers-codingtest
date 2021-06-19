def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0 :
            answer.append(i + 1)
        else : #홀수
            tmp = format(i, 'b')
            if tmp.find('0') == -1 :#모두 1
                tmp = '0' + tmp
                #앞에 0붙여주기
                
            #제일 마지막 01 찾아서 10으로 바꿔주기
            change = tmp.rfind('01')
            tmp = tmp[:change] + '10' + tmp[change+2:]
            answer.append(int(tmp,2))
                 
    return answer


