def solution(sequence, k):
    left=right=0
    answer=[0,len(sequence)]
    sum=sequence[0]
    while True:
        if sum<k:
            right+=1
            if right==len(sequence):
                break
            sum+=sequence[right]
        else:
            if sum==k:
                if right-left<answer[1]-answer[0]:
                    answer=[left,right]
            sum-=sequence[left]
            left+=1
    return answer
