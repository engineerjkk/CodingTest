def solution(k, ranges):
    answer = []
    lst=[k]
    while k>1:
        if k%2==0:
            k//=2
            lst.append(k)
        else:
            k*=3
            k+=1
            lst.append(k)
    integral=[]
    for i in range(1,len(lst)):
        integral.append((lst[i-1]+lst[i])/2)
    
    for s,e in ranges:
        e=len(integral)+e
        if e<s:
            answer.append(-1.0)
        elif e==s:
            answer.append(0.0)
        else:
            answer.append(sum(integral[s:e]))
    return answer