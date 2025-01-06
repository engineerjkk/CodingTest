import sys 
input = sys.stdin.readline 

n=int(input())
weights=list(map(int,input().split()))

def solution(weights):

    n=len(weights)

    if n<=2:
        return 0 
    
    max_energy=0 
    
    for i in range(1,n-1):
        
        current_energy=weights[i-1]*weights[i+1]
        remain_energy=weights[:i]+weights[i+1:]
        energy=current_energy+solution(remain_energy)
        max_energy=max(max_energy,energy)

    return max_energy


print(solution(weights))