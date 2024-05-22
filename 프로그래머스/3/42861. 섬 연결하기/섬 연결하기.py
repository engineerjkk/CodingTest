def solution(n, costs):
    answer=0
    costs.sort(key=lambda x:x[2])
    connect=set([costs[0][0]])
    
    while len(connect)!=n:
        for i in costs:
            if i[0] in connect and i[1] in connect:
                continue
            elif i[0] in connect or i[1] in connect:
                connect.update([i[0],i[1]])
                answer+=i[2]
                break
                
    return answer