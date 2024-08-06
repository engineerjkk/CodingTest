def solution(skill, skill_trees):
    dic={}
    answer=0
    for i in range(len(skill)):
        dic[skill[i]]=i
    for skill_tree in skill_trees:
        flag=0
        check=True
        for i in range(len(skill_tree)):
            if skill_tree[i] in dic:
                if dic[skill_tree[i]]==flag:
                    flag+=1
                else:
                    check=False
            else:
                continue
        if check:
            answer+=1
    return answer