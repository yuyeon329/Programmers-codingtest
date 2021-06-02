def solution(s):
    new_str = s.split(" ")
    answer = []
    for words in new_str:
        my_str = ""
        for i in range(len(words)):
            my_str += words[i].upper() if i % 2 == 0 else words[i].lower()
        answer.append(my_str)
                 
    return ' '.join(answer)
