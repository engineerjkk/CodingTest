from collections import Counter
def solution(want, number, discount):
    dic={}
    for i,j in zip(want,number):
        dic[i]=j
    ans=0
    for i in range(len(discount)-9):
        if dic==Counter(discount[i:i+10]):
            ans+=1
    return ans
            
 