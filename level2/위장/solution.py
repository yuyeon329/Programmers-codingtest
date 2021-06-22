def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        cloth = i[0]
        cloth_type = i[1]
        if cloth_type in dic:
            dic[cloth_type].append(cloth)
        else:
            dic[cloth_type] = [cloth]
            
    for i in dic.keys():
        answer *= len(dic[i])+1
    return answer - 1


