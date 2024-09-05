from itertools import permutations

def checkPrime(num):
    if num==2:
        return True
    if num<3 or num%2==0:
        return False
    for i in range(3,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def solution(numbers):
    answer = 0
    n=len(numbers)
    number=list(map(int,numbers.strip()))
    s=set()
    for i in range(1,n+1):
        for permu in permutations(number,i):
            num=''
            for j in permu:
                num+=str(j)
            num=int(num)
            s.add(num)
    for num in s:
        if checkPrime(num):
            print(num)
            answer+=1
    return answer