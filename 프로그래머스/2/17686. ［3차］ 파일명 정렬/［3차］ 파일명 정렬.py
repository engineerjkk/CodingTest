class File:
    def __init__(self,id,head,number,tail):
        self.id=id
        self.initial_head=head
        self.head=head.lower()
        self.initial_number=number
        self.number=int(number)
        self.tail=tail
def transform(file):
    head=""
    number=""
    tail=""
    check_head=True
    check_number=True
    for j in file:
        if check_head and not j.isdecimal():
            head+=j
        elif j.isdecimal() and check_number:
            check_head=False
            number+=j
        else:
            check_number=False
            tail+=j
    print(head,number,tail)
    return head,number,tail

def solution(files):
    dic={}
    for i in range(len(files)):
        file=files[i]
        head,number,tail=transform(file)
        dic[i]=File(i,head,number,tail)
    answer = []
    sorted_dic=sorted(dic.items(),key=lambda x:(x[1].head,x[1].number,x[1].id))
    for key,value in sorted_dic:
        name=value.initial_head+value.initial_number+value.tail
        answer.append(name)
    return answer