from itertools import product
def solution(word):
    words=["A","E","I","O","U"]
    tmp=[]
    for i in range(1,6):
        for x in list(product(words,repeat=i)):
            #print("".join(list(x)))
            tmp.append("".join(list(x)))
    tmp.sort()
    return tmp.index(word)+1
