def solution(sequence):
    answer=0
    def check(sequence,pulse):
        tmp=0
        ans=0
        for s in sequence:
            if tmp<=0:
                tmp=s*pulse
            else:
                tmp+=s*pulse
            ans=max(ans,tmp)
            pulse*=-1
        return ans
    
    answer=max(check(sequence,-1),check(sequence,1))
    return answer