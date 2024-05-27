def num(n):
    lst=[]
    for i in range(1,int(n**(0.5))+1):
        if n%i==0:
            lst.append(i)
            lst.append(n//i)
    return len(set(lst))

def solution(number, limit, power):
    lst=[]
    answer = 0
    for i in range(1,number+1):
        cnt=num(i)
        if cnt>limit:
            answer+=power
        else:
            answer+=cnt
    return answer