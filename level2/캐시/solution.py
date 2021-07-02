def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    #cacheSize가 0이 아닐 경우
    if cacheSize != 0: 
        #ref = 도시 이름
        for ref in cities:
            #대소문자 구분을 안하므로 모두 소문자 처리
            ref = ref.lower()
            
            #cache에 없는 도시라면 cache miss
            if not ref in cache:
                
                #cache가 꽉 차지 않았다면 가장 최근에 그대로 추가
                if len(cache) < cacheSize:
                    cache.append(ref)
                #cache가 꽉찼다면 가장 오래된 cache를 제거하고 가장 최근에 도시 추가    
                else:
                    cache.pop(0)
                    cache.append(ref)
                answer += 5
                
            #cache에 있는 도시라면 cache hit
            else:
                #중복되는 도시를 제거하고 가장 최근에 도시를 추가
                cache.pop(cache.index(ref))
                cache.append(ref)
                answer += 1
                
    #cacheSize가 0이란 것은 모두 cache miss라는 뜻이다. 따라서 cities의 도시 이름을 모두  cache에 넣는다.            
    else :  
        answer += len(cities)*5

    return answer
