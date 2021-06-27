import re
def solution(s):
    answer = []
    bin_num = 0
    zero_num = 0
    
    while s!= "1":
        zero_num += s.count("0")
        s = re.sub("0","",s)
        s = format(len(s),'b')
        bin_num += 1
        
    answer.append(bin_num)
    answer.append(zero_num)
    return answer


