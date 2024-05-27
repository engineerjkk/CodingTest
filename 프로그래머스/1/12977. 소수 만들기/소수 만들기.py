from itertools import combinations
def solution(nums):
    answer = 0
    nCr=combinations(nums,3)
    def sol(s):
        for i in range(2,int(s**(0.5))+1):
            if s%i==0:
                return False
        return True
    for x in nCr:
        s=sum(x)
        if sol(s):
            answer+=1


    return answer