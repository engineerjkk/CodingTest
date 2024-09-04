def solution(n, costs):
    answer = 0
    link=set([costs[0][0]])
    costs.sort(key=lambda x:x[2])
    while len(link)!=n:
        for a,b,c in costs:
            if a in link and b in link:
                continue
            if a in link or b in link:
                link.update([a,b])
                answer+=c
                break
    return answer