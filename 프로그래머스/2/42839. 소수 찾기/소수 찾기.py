from itertools import permutations
def solution(numbers):
    a=set()
    for i in range(1,len(numbers)+1):
        a|=set(map(int,map("".join,permutations(list(numbers),i))))
    a-=set(range(2))
    for i in range(2,int(max(a)**(0.5))+1):
        a-=set(range(i*2,max(a)+1,i))
    return len(a)