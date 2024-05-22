from itertools import permutations
def solution(user_id, banned_id):
    
    def check(usr,ban):
        if len(usr)!=len(ban):
            return False
        else:
            for i in range(len(usr)):
                if ban[i]=='*':
                    continue
                else:
                    if usr[i]!=ban[i]:
                        return False
        return True
    
    answer=[]
    for permu in permutations(user_id,len(banned_id)):
        
        flag=True
        for i in range(len(banned_id)):
            if not check(permu[i],banned_id[i]):
                flag=False
        
        if flag:
            if set(permu) not in answer:
                answer.append(set(permu))

        


    return len(answer)