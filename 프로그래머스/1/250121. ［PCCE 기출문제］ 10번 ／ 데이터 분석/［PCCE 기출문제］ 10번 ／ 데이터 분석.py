def solution(data, ext, val_ext, sort_by):
    dic={}
    for i in range(len(data)):
        if i not in dic:
            dic[i]=data[i]
        else:
            dic[i].append(data[i])
    lst=["code","date","maximum","remain"]
    idx=lst.index(ext)
    answer=[]
    for key, value in sorted(dic.items(),key=lambda x:x[1][lst.index(sort_by)]):
        if value[idx]>=val_ext:
            continue
        else:
            answer.append(value)
    
        
    
    return answer