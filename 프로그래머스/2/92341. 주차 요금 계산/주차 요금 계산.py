from collections import defaultdict
from math import ceil
class Parking:
    def __init__(self,fees):
        self.fees=fees
        self.in_flag=False
        self.in_time=0
        self.total=0
    def update(self,t,inout):
        if inout=="IN":
            self.in_flag=True
        else:
            self.in_flag=False
        if self.in_flag:
            self.in_time=str2int(t)
        else:
            self.total+=(str2int(t)-self.in_time)
    def calc_fee(self):
        if self.in_flag:
            self.update("23:59","out")
        add_t=self.total-self.fees[0]
        if add_t>=0:
            return self.fees[1]+ceil(add_t/self.fees[2])*self.fees[3]
        else:
            return self.fees[1]

def str2int(string):
    return int(string[:2])*60+int(string[3:])

            
def solution(fees, records):
    dic=defaultdict(lambda:Parking(fees))
    for record in records:
        t,car,inout=record.split()
        dic[car].update(t,inout)
    answer=[]
    for key,value in sorted(dic.items()):
        answer.append(value.calc_fee())
    return answer