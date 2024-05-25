def solution(n):
    watermellon="수박"
    answer=""
    for i in range(n):
        if i%2==0:
            answer+=watermellon[0]
        else:
            answer+=watermellon[1]
    
    return answer