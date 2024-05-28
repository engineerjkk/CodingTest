import copy 
def solution(X, Y):
    lst_x=[0]*10
    lst_y=[0]*10
    answer = []
    for i in X:
        lst_x[int(i)]+=1
    for i in Y:
        lst_y[int(i)]+=1
    final=""
    for idx in range(9,-1,-1):
        final+=(str(idx)*(min(lst_x[idx],lst_y[idx])))
    if len(final)==0:
        return "-1"
    if final[0]=='0':
        return '0'
    else:
        #answer=str(int(final))
        return final