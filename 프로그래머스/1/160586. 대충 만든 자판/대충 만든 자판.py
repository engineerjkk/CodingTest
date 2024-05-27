def solution(keymap, targets):
    answer = []
    for i in range(len(targets)):
        cnt=0
        for t in targets[i]:
            lst=[]
            for k in keymap:
                for l in range(len(k)):
                    if t==k[l]:
                        lst.append(l+1)
            if len(lst)!=0:
                MIN=min(lst)
                cnt+=MIN
            else:
                cnt=-1
                break
        answer.append(cnt)
    return answer