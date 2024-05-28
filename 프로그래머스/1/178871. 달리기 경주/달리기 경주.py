def solution(players, callings):
    dic={}
    for i,calling in enumerate(players):
        dic[calling]=i
    for calling in callings:
        idx=dic[calling]
        dic[players[idx-1]]+=1
        dic[calling]-=1
        players[idx-1],players[idx]=players[idx],players[idx-1]
    return players