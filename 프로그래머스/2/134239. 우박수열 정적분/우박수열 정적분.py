def solution(k, ranges):
    answer = []
    lst=[k]
    while k>1:
        if k%2==0:
            k=k/2
            lst.append(k)
        else:
            k=k*3+1
            lst.append(k)
    integral=[]
    for i in range(len(lst)-1):
        integral.append((lst[i]+lst[i+1])/2)
    for s,e in ranges:
        e=len(integral)+e
        if e<s:
            answer.append(-1)
        elif e==s:
            answer.append(0)
        else:
            answer.append(sum(integral[s:e]))
    return answer