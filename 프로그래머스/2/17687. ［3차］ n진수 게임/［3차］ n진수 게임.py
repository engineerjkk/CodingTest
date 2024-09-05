def transform(num,i):
    numOver={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    ret=''
    while num>0:
        remainder=num%i
        if remainder>=10:
            ret+=numOver[remainder]
        else:
            ret+=str(remainder)
        num=num//i
    return ret[::-1]

def solution(n, t, m, p):
    
    answer = ''
    tmp='0'
    for i in range(1,t*m):
        tmp+=transform(i,n)
    
    p-=1
    while p<len(tmp):
        if len(answer)==t:
            return answer
        answer+=tmp[p]
        p+=m
        
    return answer