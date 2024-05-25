def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        tmp=[]
        for j in range(1,i+1):
            if i%j==0:
                tmp.append(j)
        if len(tmp)%2==0:
            answer+=i
        else:
            answer-=i
    return answer