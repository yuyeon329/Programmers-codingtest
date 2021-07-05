from itertools import combinations
def solution(info, query):
    answer = []
    db = {}
    
    #정보 목록을 순회하며
    for i in info :
        #지원자의 정보를 공백 기준으로 잘라 tmp에 저장
        tmp = i.split()
        #언어, 직군, 경력, 소울푸드를 conditions에 저장
        conditions = tmp[:-1]
        #점수는 따로 저장
        score = int(tmp[-1])
        
        #조건들에 대해
        for n in range(5):
            #4개의 조건들에 대해 모든 조합 구하기
            combi = list(combinations(range(4),n))
            #각 조합들에 대해
            for c in combi:
                #'-'이 포함된 조합을 만들기 위해 복사
                copy_c = conditions.copy()
                #ex) (0,2)-> [-,~,-,~]
                for v in c:
                    #'-'이 포함된 조건 생성
                    copy_c[v] = '-'
                #"/"으로 구분된 조건 changed_t_c 생성
                changed_copy_c = '/'.join(copy_c)
                #생성된 조건에 만족하는 점수를 추가해줌.
                if changed_copy_c in db:
                    db[changed_copy_c].append(score)
                else:
                    db[changed_copy_c] = [score]
    
    #점수를 기준으로 정렬
    for v in db.values():
        v.sort()
    
    #쿼리의 모든 조건에 대해서
    for q in query:
        #쿼리를 정리해주고
        qry = [i for i in q.split() if i != 'and']
        #조건처럼 /로 구분할 수 있게 정리
        qry_cnds = '/'.join(qry[:-1])
        #점수는 역시 따로 저장
        qry_score = int(qry[-1])
        #만약 쿼리 조건이 db 딕셔너리에 있다면
        if qry_cnds in db:
            #해당 조건의 점수를 가져옴
            data = db[qry_cnds]
            #lower bound 알고리즘을 이용해 쿼리의 점수보다 높거나 같은 점수인
            #사람이 처음 나타나는 인덱스 찾기
            if len(data)> 0:
                l, r = 0, len(data)
                while l<r:
                    if data[(l+r) //2] >= qry_score:
                        r = (l+r)//2
                    else:
                        l = (l+r) // 2 + 1
                #qry_score보다 높은 점수를 받은 사람 명수를 answer에 추가     
                answer.append(len(data)-l)
        else:
            answer.append(0)
        
    return answer
