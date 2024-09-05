def solution(sequence, k):
    answer = [0,len(sequence)]
    left=0
    right=0
    num=sequence[0]
    while right<len(sequence):
        if num<k:
            right+=1
            if right>=len(sequence):
                break
            num+=sequence[right]
        else:
            if num==k:
                if right-left<answer[1]-answer[0]:
                    answer=[left,right]
            num-=sequence[left]
            left+=1
    return answer