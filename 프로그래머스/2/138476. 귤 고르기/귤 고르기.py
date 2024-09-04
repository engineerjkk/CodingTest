from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter=Counter(tangerine)
    counter=sorted(counter.items(),key=lambda x:x[1],reverse=True)
    for key,value in counter:
        k-=value
        answer+=1
        if k<=0:
            return answer 
    return answer