from itertools import product
def solution(word):
    lst=['A','E','I','O','U']
    tmp=[]
    for i in range(1,6):
        for pro in product(lst,repeat=i):
            tmp.append(''.join(pro))
    tmp.sort()
    answer=tmp.index(word)+1
    return answer