def solution(arr):
    return sum(arr) / len(arr)
    """
    answer = 0
    length = len(arr)
    sum = 0
    for i in range(length):
        sum += arr[i]
    answer = sum/length

    return answer
    """
    #return sum(arr[i] for i in range(len(arr))) / len(arr)
