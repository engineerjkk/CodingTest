def solution(tickets):
    dic={}
    for s,e in tickets:
        if s not in dic:
            dic[s]=[e]
        else:
            dic[s].append(e)
    for key in dic:
        dic[key].sort()
    
    s=["ICN"]
    p=[]
    while s:
        tar=s[-1]
        if tar in dic and dic[tar]:
            s.append(dic[tar].pop(0))
        else:
            p.append(s.pop())
    return p[::-1]