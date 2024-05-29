def solution(n, words):
    cnt=0
    dic={}
    dic2={}
    tmp=[]
    for i,word in enumerate(words):
        cnt+=1
        #끝말잇기 규칙 실패 경우
        if tmp and tmp[-1]!=word[0] :
            if cnt in dic2:
                return [cnt,dic2[cnt]+1]
            else:
                return [cnt,1]
        #         return [cnt,1]
        ##몇번째 사람이 탈락하는지 출력
        if word in dic:
            if cnt in dic2:
                return [cnt,dic2[cnt]+1]
            else:
                return [cnt,1]
        else:
            dic[word]=i+1
        # 몇번째말하는건지 입력
        if cnt in dic2:
            dic2[cnt]+=1
        else:
            dic2[cnt]=1
        if cnt>n-1:
            cnt=0
        tmp=word

    return [0,0]