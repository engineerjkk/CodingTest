from itertools import combinations
def solution(numbers):
    nCr=combinations(numbers,2)
    answer=[]
    for a,b in nCr:
        answer.append(a+b)
    answer=sorted(list(set(answer)))
    return answer