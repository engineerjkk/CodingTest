from collections import Counter
def solution(weights):
    counter=Counter(weights)
    answer=0
    for key,value in counter.items():
        if value>=2:
            answer+=value*(value-1)//2
    weights=set(weights)
    #2:3,2:4,3:4
    for w in weights:
        if w*2/3 in weights:
            answer+=counter[w*2/3]*counter[w]
        if w*2/4 in weights:
            answer+=counter[w*2/4]*counter[w]
        if w*3/4 in weights:
            answer+=counter[w*3/4]*counter[w]
    return answer