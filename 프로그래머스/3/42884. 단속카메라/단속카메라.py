import sys
def solution(routes):
    key=-30001
    answer=0
    routes.sort(key=lambda x:x[1])
    for s,e in routes:
        if s>key:
            answer+=1
            key=e
    return answer
