def transform(s):
    ret=[]
    for i in range(len(s)-1):
        a=s[i]+s[i+1]
        if a.isalpha():
            ret.append(a)
    return ret
        
def solution(str1, str2):
    str1,str2=transform(str1.upper()),transform(str2.upper())
    intersection=[]
    for s in str1:
        if s in str2:
            str2.remove(s)
            intersection.append(s)
    union=str1+str2
    if len(union)==0:
        return 65536
    answer= int((len(intersection)/len(union))*65536)
    return answer
    




    
