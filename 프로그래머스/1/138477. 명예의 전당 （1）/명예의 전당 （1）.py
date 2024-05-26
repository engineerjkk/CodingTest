def solution(k, score):
    answer = []
    tmp=[]
    for i in score:
        if len(tmp)<k:
            tmp.append(i)
            answer.append(min(tmp))
        else:
            if i<min(tmp):
                answer.append(min(tmp))
            else:
                tmp.remove(min(tmp))
                tmp.append(i)
                answer.append(min(tmp))
    return answer