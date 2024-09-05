from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic={}
    for i,j in zip(want,number):
        dic[i]=j
    ans=0
    for i in range(len(discount)-9):
        if dic==Counter(discount[i:i+10]):
            answer+=1
    return answer