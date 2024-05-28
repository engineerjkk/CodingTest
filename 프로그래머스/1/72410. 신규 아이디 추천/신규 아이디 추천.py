def solution(new_id):
    answer = ''
    check="abcdefghijklmnopqrstuvwxyz0123456789-_."
    #1단계
    print(new_id)
    new_id=new_id.lower()
    print(new_id)
    #2단계
    tmp=""
    for i in new_id:
        if i in check:
            tmp+=i
    new_id=tmp
    #3단계
    while True:
        if ".." in new_id:
            new_id=new_id.replace("..",".")
        else:
            break

    #4단계
    while len(new_id)>0:
        if new_id[0]==".":
            new_id=new_id[1:]
        else:
            break
    while len(new_id)>0:
        if new_id[-1]==".":
            new_id=new_id[:-1]
        else:
            break
    #5단계
    if len(new_id)==0:
        new_id+="a"

    #6단계

    if len(new_id)>15:
        new_id=new_id[:15]
        while True:
            if new_id[-1]!=".":
                break
            else:
                new_id=new_id[:-1]
            
    if len(new_id)<=2:
        a=new_id[-1]
        while True:
            new_id+=a
            if len(new_id)==3:
                break
            
    return new_id