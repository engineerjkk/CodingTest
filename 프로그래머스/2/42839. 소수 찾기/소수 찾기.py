from itertools import permutations
def solution(numbers):
    s=set()
    for i in range(1,len(numbers)+1):
        s|=set(map(int,map("".join,permutations(list(numbers),i))))
    s-=set(range(2))
    for i in range(2,int(max(s)**(0.5))+1):
        s-=set(range(i*2,max(s)+1,i))
    return len(s)