"""
def solution(x):
    answer = True
    mystr = str(x)
    sum = 0
    for i in range(len(mystr)):
        sum += int(mystr[i])
    if x % sum != 0:
        answer = False
    return answer
 """   
def solution(x):
    return x % sum(int(i) for i in str(x)) == 0
