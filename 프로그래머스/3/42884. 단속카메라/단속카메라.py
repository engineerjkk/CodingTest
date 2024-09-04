def solution(routes):
    answer = 0
    key=-30001
    routes.sort(key=lambda x:x[1])
    for s,e in routes:
        if key<s:
            key=e
            answer+=1
    return answer