def solution(skill, skill_trees):
    answer = 0
    if len(skill_trees) == 1 and skill != skill_trees[0]:
        return 1
    
    for i in skill_trees:
        tmp = ''
        for j in i:
            if j in list(skill):
                tmp+=j
        if skill.startswith(tmp):
            answer +=1

    return answer
