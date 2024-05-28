def solution(id_list, report, k):
    answer = []
    dic={}
    for name in id_list:
        if name not in dic:
            dic[name]=[]
    #신고한거 dic에 정리, 한 사람이 동일한 사람을 2번이상 할 수 없음
    for ing_ed in report:
        ing,ed = ing_ed.split()
        if ed not in dic[ing]:
            dic[ing].append(ed)
    #신고 당한거 누적해서 정리
    lst=[0]*len(id_list)
    for i,(key,value) in enumerate(dic.items()):
        for v in value:
            lst[id_list.index(v)]+=1
    #신고 당해서 실제 정지당했는지 체크
    mail_ed=[0]*(len(id_list))
    for i in range(len(lst)):
        if lst[i]>=k:
            mail_ed[i]=1
    
    #신고한 사람이 진짜 정지를 당했는지 체크
    mail_ing=[0]*len(id_list)
    for key,value in dic.items():
        for v in value:
            if mail_ed[id_list.index(v)]==1:
                mail_ing[id_list.index(key)]+=1
    
        
    return mail_ing