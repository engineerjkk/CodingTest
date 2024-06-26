def solution(new_id):
    answer = ''
    removed=["-","_","."]
    for i in new_id:
        if i.isalpha() or i.isdecimal() or i in removed:
            answer+=i
    answer=answer.lower()
    cnt=0
    while True:
        check=True
        if ".." in answer:
            answer=answer.replace("..",".")
            check=False
        if answer[0]==".":
            answer=answer[1:]
            check=False
        elif answer[-1]==".":
            answer=answer[:-1]
            check=False
        if len(answer)==0:
            answer+="a"
            check=False

        if check:
            break
    tmp=answer[-1]
    while len(answer)<3:
        answer+=tmp
        
    if len(answer)>15:
        answer=answer[:15]
        check=False
        if answer[-1]==".":
            answer=answer[:-1]
    return answer