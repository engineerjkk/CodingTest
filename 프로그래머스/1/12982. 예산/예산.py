def solution(d, budget):
    d.sort()
    answer=0
    for i in d:
        if (budget-i)<0:
            return answer
        budget-=i
        answer+=1
    return answer
