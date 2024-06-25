from collections import defaultdict
from math import ceil
class Parking:
    def __init__(self,fees):
        self.fees=fees
        self.flag=False
        self.time=0
        self.total=0
    def update(self,t,inout):
        if inout=="IN":
            self.flag=True
        else:
            self.flag=False
        if self.flag:
            self.time=str2int(t)
        else:
            self.total+=(str2int(t)-self.time)
    def cal_fee(self):
        if self.flag:
            self.update("23:59","out")
        add_time=self.total-self.fees[0]
        if add_time>=0:
            return self.fees[1]+ceil(add_time/self.fees[2])*self.fees[3]
        else:
            return self.fees[1]
    
def str2int(string):
    return int(string[:2])*60+int(string[3:])

def solution(fees,records):
    dic=defaultdict(lambda:Parking(fees))
    for record in records:
        time, car, inout = record.split()
        dic[car].update(time,inout)
    answer=[]
    for key,value in sorted(dic.items()):
        answer.append(dic[key].cal_fee())
    return answer
