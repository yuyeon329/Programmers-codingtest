import itertools 

def solution(numbers):
    answer = 0
    nCr_list = set()
    for i in range(len(numbers)):
        nCr_list.update(map(int,map(''.join,itertools.permutations(list(numbers),i+1))))
    
    for i in nCr_list:
        if i <= 1 :
            answer += 1
        else:   
            for j in range(2,int(i**.5)+1):
                    if i%j == 0:
                        answer += 1
                        break

    return len(nCr_list) - answer
