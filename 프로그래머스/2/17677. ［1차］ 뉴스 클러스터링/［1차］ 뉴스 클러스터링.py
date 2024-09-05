import copy
def solution(str1, str2):
    answer=0
    def transform(string):
        ret=[]
        for i in range(1,len(string)):
            a=string[i-1]+string[i]
            if a.isalpha():
                ret.append(a)
        return ret
    
    total1,total2=transform(str1.lower()),transform(str2.lower())
    intersection=[]
    for t1 in total1:
        if t1 in total2:
            total2.remove(t1)
            intersection.append(t1)
    
    union=list(total1+total2)
    if len(union)==0:
        return 65536
    answer=int((len(intersection)/len(union))*65536)
    return answer