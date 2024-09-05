def solution(n, k):
    def transform(num,k):
        dic={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        tmp=''
        while num:
            remainder=num%k
            # if remainder>=10:
            #     tmp+=dic[remainder]
            # else:
            tmp+=str(remainder)
            num//=k
        return tmp[::-1]
    
    def checkPrime(n):
        if n==2 or n==3:
            return True
        if n%2==0 or n<2:
            return False
        for i in range(3,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    
    num=transform(n,k)
    num=num.split('0')
    answer = 0
    for n in num:
        if n=='':
            continue
        if checkPrime(int(n)):
            answer+=1
    return answer