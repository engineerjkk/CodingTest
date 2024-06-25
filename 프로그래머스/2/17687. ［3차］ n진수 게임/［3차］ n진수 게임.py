  
def transform(num,n):
    if num==0:
        return "0"
    numOver={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    ret=""
    while num>0:
        remainder=num%n
        if remainder>=10:
            ret+=numOver[remainder]
        else:
            ret+=str(remainder)
        num=num//n
    return ret[::-1]
        
def solution(n, t, m, p):
    total=""
    for i in range(t*m):
        total+=transform(i,n)
    p-=1
    answer=""
    while True:
        if len(answer)==t:
            return answer
        answer+=total[p]
        p+=m
        
    


        