def solution(sequence):
    def check(seq,pulse):
        answer = -1
        tmp=0
        for i in seq:
            if tmp<=0:
                tmp=i*pulse
            else:
                tmp+=i*pulse
            pulse*=-1
            answer=max(answer,tmp)
        return answer
    answer=max(check(sequence,-1),check(sequence,1))
    return answer