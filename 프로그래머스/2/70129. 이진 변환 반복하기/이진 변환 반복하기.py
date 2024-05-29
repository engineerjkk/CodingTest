def solution(s):
    answer = []
    cnt=0
    total=0
    while True:
        if "0" in s:
            tmp=s.replace("0","")
        else:
            tmp=s
        diff=len(s)-len(tmp)
        s=str(bin(len(tmp))[2:])
        cnt+=1
        total+=diff
        if s=="1":
            return [cnt,total]
