
def convert(i,n):
    numOver={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    s=""
    if i==0:
        return "0"
    while i>0:
        num=i%n
        if num>=10:
            s+=numOver[num]
        else:
            s+=str(num)
        i=i//n
    return s[::-1]

def solution(n, t, m, p):
    answer=''
    s=''
    for i in range(t*m):
        s+=convert(i,n)
    p-=1
    while p<len(s):
        if len(answer)==t:
            break
        answer+=s[p]
        p+=m
    return answer
        