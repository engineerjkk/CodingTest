from itertools import product
def solution(word):
    lst=["A","E","I","O","U"]
    answer=[]
    for i in range(1,6):
        for pro in product(lst,repeat=i):
            answer.append("".join(pro))
    answer.sort()
    return answer.index(word)+1