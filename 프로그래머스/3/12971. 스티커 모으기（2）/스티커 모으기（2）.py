def solution(sticker):
    
    if len(sticker)<=3:
        return max(sticker)
    
    #첫번째 카드를 선택한경우
    dp1=[0]*len(sticker)
    dp1[0],dp1[1]=sticker[0],max(sticker[0],sticker[1])
    for i in range(2,len(sticker)-1):
        dp1[i]=max(dp1[i-1],dp1[i-2]+sticker[i])
    
    #첫번째 카드를 선택하지않은경우
    dp2=[0]*len(sticker)
    dp2[0],dp2[1]=0,sticker[1]
    for i in range(2,len(sticker)):
        dp2[i]=max(dp2[i-1],dp2[i-2]+sticker[i])

    return max(dp1[-2],dp2[-1])