from collections import Counter
def solution(want, number, discount):
    dic={}
    for i,j in zip(want,number):
        dic[i]=j
    answer=0
    for i in range(len(discount)-9):
        if dic==Counter(discount[i:i+10]):
            answer+=1
    return answer        
 