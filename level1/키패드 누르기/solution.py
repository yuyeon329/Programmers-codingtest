def solution(numbers, hand):
    dic = {1:[0,0], 2:[0,1], 3:[0,2],
           4:[1,0], 5:[1,1], 6:[1,2],
           7:[2,0], 8:[2,1], 9:[2,2],
          '*':[3,0], 0:[3,1], '#':[3,2]}
    
    answer = ''
    l = dic['*']
    r = dic['#']
    
    for i in numbers:
        now = dic[i]
        if i in [1,4,7]:
            answer +='L'
            l = dic[i]
            
        elif i in [3,6,9]:
            answer +='R'
            r = dic[i]
            
        else :
            l_distance = 0
            r_distance = 0
            
            for x,y,z in zip(l,r,now):
                l_distance += abs(x-z)
                r_distance += abs(y-z)
                
            if l_distance == r_distance:
                if hand == "left":
                    answer += "L"
                    l = dic[i]
                else:
                    answer += "R"
                    r = dic[i]
            elif l_distance < r_distance:
                    answer += "L"
                    l = dic[i]
            else:
                answer += "R"
                r = dic[i]
                
    return answer
