
def transform(str1):
    tmp=[]
    for i in range(len(str1)-1):
        a=str1[i]+str1[i+1]
        if a.isalpha():
            tmp.append(a)
    return tmp

def solution(str1, str2):
    str1,str2=transform(str1.upper()),transform(str2.upper())
    intersection=[]
    for i in str1:
        if i in str2:
            str2.remove(i)
            intersection.append(i)
    union=str1+str2
    if len(union)==0:
        return 65536
    answer=int((len(intersection)/len(union))*65536)
    return answer


    
