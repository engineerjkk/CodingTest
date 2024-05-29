def solution(arr):
    answer = 0
    def check(arr,n):
        return
    num=1
    for i in arr:
        num*=i
    for i in range(max(arr),int(num)+1):
        tmp=[]
        for j in arr:
            if i%j==0:
                tmp.append(True)
            else:
                continue
        if len(tmp)==len(arr):
            return i
    return answer