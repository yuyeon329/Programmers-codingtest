def solution(citations):
    tmp = 0
    citations.sort(reverse = True)
    for i in range(len(citations)):
          if i + 1  <= citations[i] :
            tmp = i + 1
    return tmp
