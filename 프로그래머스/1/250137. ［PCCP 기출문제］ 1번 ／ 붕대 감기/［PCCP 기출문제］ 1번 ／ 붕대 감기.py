from collections import deque
def solution(bandage, health, attacks):
    t,x,y=bandage
    attacks=deque(attacks)
    now_time=0
    cnt=0
    now=health
    attack_time,attack=attacks.popleft()
    check=False
    while True:
        now_time+=1
        if now_time==attack_time:
            now-=attack
            if now<=0:
                return -1
            cnt=0
            if attacks:
                attack_time,attack=attacks.popleft()
                if now<=0:
                    return -1
            else:
                if now<=0:
                    return -1
                else:
                    return now
                
        else:
            cnt+=1
            now+=x
            if now>health:
                now=health
            if cnt==t:
                cnt=0
                now+=y
                if now>health:
                    now=health

            if now<=0:
                return -1
            
