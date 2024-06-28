from collections import defaultdict
from math import ceil
class Parking:
    def __init__(self,fees):
        self.fees=fees
        self.flag=False
        self.time=0
        self.total=0
    def update(self,time,inout):
        if inout=="IN":
            self.flag=True
            self.time=str2int(time)
        else:
            self.flag=False
            self.total+=(str2int(time)-self.time)
    def cal_price(self):
        if self.flag:
            self.update("23:59","OUT")
        add_price=self.total-self.fees[0]
        if add_price>0:
            return self.fees[1]+ceil(add_price/self.fees[2])*self.fees[3]
        else:
            return self.fees[1]
def str2int(string):
    return int(string[:2])*60+int(string[3:])

def solution(fees, records):
    dic=defaultdict(lambda:Parking(fees))
    for record in records:
        time,car,inout=record.split()
        dic[car].update(time,inout)
    answer=[]
    for key,value in sorted(dic.items()):
        answer.append(value.cal_price())
    return answer