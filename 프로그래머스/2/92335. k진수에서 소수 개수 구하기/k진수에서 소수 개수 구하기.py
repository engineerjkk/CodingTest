def n_to_k(n,k):
    ret=""
    while n>0:
        ret+=str(n%k)
        n=n//k
    return ret[::-1]

def check_prime(n):
    if n==2 or n==3:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(3,int(n**(0.5))+1,2):
        if n%i==0:
            return False
    return True

def solution(n, k):
    num_k=n_to_k(n,k)
    num_k=num_k.split("0")
    answer=0
    for i in num_k:
        if i=="":
            continue
        if check_prime(int(i)):
            answer+=1
    return answer
        



