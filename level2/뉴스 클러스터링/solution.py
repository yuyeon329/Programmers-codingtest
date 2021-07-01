def solution(str1, str2):
    answer = 1
    str1 = str1.lower()
    str2 = str2.lower()
    l_intersection = 0
    l_union = 0
    
    if str1 == str2 :
        return answer*65536
    
    s1 = []
    s2 = []
    common = []
    
    for i in range(len(str1)-1):
        tmp = str1[i] + str1[i+1]
        if tmp.isalpha():
            s1.append(tmp)
            
    for i in range(len(str2)-1):
        tmp = str2[i] + str2[i+1]
        if tmp.isalpha():
            s2.append(tmp)
            
    s1_copy = s1.copy()
    s1_copy2 = s1.copy()
    
    for i in s2:
        s1_copy2.append(i) if i not in s1_copy else s1_copy.remove(i)
    l_union = len(s1_copy2)
    
    for i in s2:
        if i in s1:
            s1.remove(i)
            common.append(i)
    l_intersection = len(common)
    
    return int(l_intersection/l_union * 65536)
