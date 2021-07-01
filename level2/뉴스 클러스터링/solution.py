def solution(str1, str2):
    #대문자와 소문자의 차이는 무시하므로 모두 소문자로 바꿔준다.
    str1 = str1.lower()
    str2 = str2.lower()
    
    #다중집합의 합집합과 교집합을 구하기 위한 변수 선언
    s1,s2,common = [], [], []
    l_union, l_intersection = 0, 0
    
    #소문자로 바꿔준 결과가 같다면 자카드 유사도는 1이므로 65536리턴
    if str1 == str2 :
        return 65536
    
    #입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다.
    #이때 영문자로 된 글자 쌍만 유효하므로 isalpha()사용
    for i in range(len(str1)-1):
        tmp = str1[i] + str1[i+1]
        if tmp.isalpha():
            s1.append(tmp)
            
    for i in range(len(str2)-1):
        tmp = str2[i] + str2[i+1]
        if tmp.isalpha():
            s2.append(tmp)
    
    #다중집합의 합집합을 만들기 위해 깊은 복사로 s1_copy, s1_copy2 생성
    s1_copy = s1.copy()
    s1_copy2 = s1.copy()
    
    #다중집합의 합집합을 구해준다.
    for i in s2:
        s1_copy2.append(i) if i not in s1_copy else s1_copy.remove(i)
    l_union = len(s1_copy2)
    
    #다중집합의 교집합을 구해준다.
    for i in s2:
        if i in s1:
            s1.remove(i)
            common.append(i)
    l_intersection = len(common)
    
    #자카드 유사도를 구한 후, 65536을 곱한 다음에 소수점 아래는 버려준 후 return
    return int(l_intersection/l_union * 65536)
