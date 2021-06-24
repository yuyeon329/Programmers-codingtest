def solution(progresses, speeds):
    answer = []
    pairs = [pair for pair in zip(progresses, speeds)]
    stack = []
    count = 0
    for i in range(len(pairs)):
        n,q = divmod(100-pairs[i][0],pairs[i][1])
        if q > 0:
            n+=1
        stack.append(n)
    
    for i,day in enumerate(stack):
        if i == 0:
            max = day
            answer.append(1)
            continue
        if day <= max:
            answer[-1]+=1
        else:
            max = day
            answer.append(1)
    return answer
