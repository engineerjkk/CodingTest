from collections import deque
def solution(answers):
    answer = []
    person_k=deque([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    person_q=deque([2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5])
    person_v=deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    answers=deque(answers)
    cnt_k,cnt_q,cnt_v=0,0,0
    while len(answers)>0:
        k,q,v=person_k.popleft(),person_q.popleft(),person_v.popleft()
        a=answers.popleft()
        if k==a:
            cnt_k+=1
        if q==a:
            cnt_q+=1
        if v==a:
            cnt_v+=1
        person_k.append(k)
        person_q.append(q)
        person_v.append(v)
    answer=[]
    person=[cnt_k,cnt_q,cnt_v]
    for idx,p in enumerate(person):
        if p==max(person):
            answer.append(idx+1)
    
        
        
    return answer