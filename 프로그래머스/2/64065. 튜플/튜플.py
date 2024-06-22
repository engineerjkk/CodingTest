def solution(s):
    s=s[2:-2].split("},{")
    tmp=[]
    for i in s:
        tmp.append(list(map(int,i.split(","))))
    tmp.sort(key=lambda x:len(x))
    answer=[]
    for tm in tmp:
        for t in tm:
            if t not in answer:
                answer.append(t)
    return answer

