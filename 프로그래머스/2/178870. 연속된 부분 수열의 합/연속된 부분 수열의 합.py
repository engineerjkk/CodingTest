def solution(sequence, k):
    answer = [0,len(sequence)]
    left=right=0
    sum=sequence[0]
    while right<len(sequence):
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