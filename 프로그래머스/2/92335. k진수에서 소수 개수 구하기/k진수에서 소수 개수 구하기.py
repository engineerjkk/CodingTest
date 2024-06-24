def transform(num,k):
    numOver={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    ret=""
    while num>0:
        remainder=num%k
        if remainder>=10:
            ret+=numOver[remainder]
        else:
            ret+=str(remainder)
        num=num//k
    return ret[::-1]

def check_prime(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for i in range(3,int(num**(0.5))+1):
        if num%i==0:
            return False
    return True
    
            

def solution(n, k):
    k_num=transform(n,k)
    k_num=k_num.split("0")
    tmp=[]
    ans=0
    for s in k_num:
        if s=="":
            continue
        tmp.append(list(map(int,s.split(","))))
    for i in range(len(tmp)):
        for j in tmp[i]:
            if check_prime(int(j)):
                ans+=1
    return ans
