def solution(str1, str2):
    answer = 0
    def transform(cluster):
        ret=[]
        for i in range(1,len(cluster)):
            a=cluster[i-1]+cluster[i]
            if a.isalpha():
                ret.append(a)
        return ret
    str1,str2=transform(str1.lower()),transform(str2.lower())
    intersection=[]
    for s in str1:
        if s in str2:
            str2.remove(s)
            intersection.append(s)
    union=str1+str2
    if len(union)==0:
        return 65536
    answer=int((len(intersection)/len(union))*65536)
    return answer