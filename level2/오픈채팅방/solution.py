def solution(record):
    answer = []
    result = [] 
    id_list = {} #유저아이디의 닉네임을 담는 딕셔너리
    
    #record의 기록을 순회하며
    for i in record:
        #공백을 기준으로 활동, uid, 닉네임을 잘라준다.
        tmp = i.split(" ")
        
        #입장
        if tmp[0] == "Enter":
            #유저아이디와 닉네임을 저장하고, 닉네임은 추후에 변경될 수 있으므로 유저아이디 + 활동으로 기록한다.
            id_list[tmp[1]] = tmp[2]
            result.append([tmp[1],"님이 들어왔습니다."])
        
        #퇴장
        elif tmp[0] == "Leave":
            #닉네임은 추후에 변경될 수 있으므로 유저아이디 + 활동으로 기록한다.
            result.append([tmp[1],"님이 나갔습니다."])
        
        #닉네임 변경
        else :
            #딕셔너리의 uid 키값을 찾아 값을 변경해준다.
            id_list[tmp[1]]= tmp[2]

    for i in result:
        #기록의 uid를 record의 모든 기록을 순회하고 마친 최종적인 닉네임으로 바꿔준다.
        i[0] = id_list[i[0]]
        #문자열을 붙여준 후
        i = "".join(i)
        #answer에 추가한다.
        answer.append(i)

    return answer
