def transform(num,n):
    if num==0:
        return "0"
    ret=""
    numOver={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    while num>0:
        remainder=num%n
        if remainder>=10:
            ret+=numOver[remainder]
        else:
            ret+=str(remainder)
        num=num//n
    return ret[::-1]

def solution(n, t, m, p):
    answer = ''
    result=""
    for i in range(t*m):
        result+=transform(i,n)
    p-=1
    while True:
        if len(answer)==t:
            break
        answer+=result[p]
        p+=m
    return answer