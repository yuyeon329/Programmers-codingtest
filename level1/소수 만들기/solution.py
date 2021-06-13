from itertools import combinations

def solution(nums):
    combi = list(combinations(nums,3))
    count = 0
    
    for i in combi:
        sum_i = sum(i)
        for j in range(2,int(sum_i **.5) +1):
            if sum_i % j == 0:
                count+=1
                break

    return len(combi)-count
