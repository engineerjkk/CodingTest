from itertools import permutations
def check(per,ban):
    if len(per)!=len(ban):
        return False
    for i in range(len(per)):
        if ban[i]=='*':
            continue
        if per[i]!=ban[i]:
            return False
    return True
def solution(user_id, banned_id):

    answer = []
    for permu in permutations(user_id,len(banned_id)):
        flag=True
        for i in range(len(permu)):
            if not check(permu[i],banned_id[i]):
                flag=False
        if flag:
            if set(permu) not in answer:
                answer.append(set(permu))
    return len(answer)