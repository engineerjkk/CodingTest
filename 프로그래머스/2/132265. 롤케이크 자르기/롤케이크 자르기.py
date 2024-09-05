from collections import Counter
def solution(topping):
    answer = 0
    bro=Counter(topping)
    chulsu=set()
    for t in topping:
        chulsu.add(t)
        bro[t]-=1
        if bro[t]==0:
            bro.pop(t)
        if len(chulsu)==len(bro):
            answer+=1
        
    return answer