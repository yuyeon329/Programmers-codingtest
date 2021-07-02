def solution(s):
    answer = 0
    tmp = ''
    candidates = []
    
    #압축할 문자열의 길이가 1이면 return 1
    if len(s) == 1:
        return 1
    
    #문자열의 절반 단위까지 나눠봄
    for i in range(1,len(s)//2 + 1 ):
        
        cnt = 1
        #문자열을 자름
        tmpStr = s[:i]
        #단위만큼 잘라나감
        for j in range(i, len(s), i):
            #다음 단위가 같다면 cnt += 1
            if s[j:j+i] == tmpStr:
                cnt += 1
            #다음 단위가 다르다면    
            else:
                #만약 압축이 되지 않았다면 한번만 나타난 경우 1은 생략하므로 cnt = ""
                if cnt == 1:
                    cnt = ""
                #압축이 된 횟수 + 단위     
                tmp += str(cnt)+tmpStr
                #다음 비교를 위해 변수 초기화
                tmpStr = s[j:j+i]
                cnt = 1
                
        #마지막 잘린 단위까지 처리하기 위해 
        if cnt == 1:
            cnt = ""
        tmp += str(cnt) + tmpStr
        
        #압축된 문자열의 길이를 저장 후 tmp 초기화
        candidates.append(len(tmp))
        tmp = ""
        
        #가장 압축이 잘 된 문자열의 길이 return 
    return min(candidates)
