class User:
    def __init__(self,name):
        self.name=name
    def status(self,flag):
        if flag=="Enter":
            return self.name+"님이 들어왔습니다."
        elif flag=="Leave":
            return self.name+"님이 나갔습니다."
def solution(records):
    dic={}
    for record in records:
        record=record.split()
        if len(record)==2:
            flag,id=record
        elif len(record)==3:
            flag,id,name=record
            dic[id]=User(name)
    answer=[]
    for record in records:
        record=record.split()
        if len(record)==2:
            flag,id=record
        elif len(record)==3:
            flag,id,name=record
        if flag !="Change":
            answer.append(dic[id].status(flag))
    return answer