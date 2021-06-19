def solution(people, limit):
    tmp = len(people)//2
    people.sort()
    i , j = 0, len(people) -1
    answer = 0
    
    while i <= j :
        answer += 1
        if people[i] + people[j] <= limit :
            i += 1
        j -= 1
            
    return answer
