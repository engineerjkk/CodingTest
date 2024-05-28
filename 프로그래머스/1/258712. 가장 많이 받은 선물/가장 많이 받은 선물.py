def solution(friends, gifts):
    
    #주고받은 선물
    n=len(friends)
    graph=[[0]*n for _ in range(n)]
    check=[[0]*n for _ in range(n)]
    for left_right in gifts:
        left,right=left_right.split()
        idx_left=friends.index(left)
        idx_right=friends.index(right)
        graph[idx_left][idx_right]+=1
        # 더 많이 줬는지 체크
        check[idx_left][idx_right]+=1
        check[idx_right][idx_left]-=1
        
    
    #선물 지수
    dic={}
    for friend in friends:
        if friend not in dic:
            dic[friend]=[0]*2
    ##준선물,받은선물 체크
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            else:
                if graph[i][j]>0:
                    dic[friends[i]][0]+=graph[i][j]
                    dic[friends[j]][1]+=graph[i][j]
    
    ##선물지수까지 체크
    final_dic={}
    for key,value in dic.items():
        if key not in final_dic:
            final_dic[key]=value[0]-value[1]
    
    answer_lst=[0]*n
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            else:
                if check[i][j]>0:
                    answer_lst[i]+=1
                elif check[i][j]==0:
                    if final_dic[friends[i]]>final_dic[friends[j]]:
                        answer_lst[i]+=1
    answer=max(answer_lst)
    return answer