def solution(s):
    s=s[2:-2].split("},{")
    tmp=[]
    for i in s:
        tmp.append(list(map(int,i.split(","))))
    tmp.sort(key=lambda x:len(x))
    ans=[]
    for i in range(len(tmp)):
        for j in tmp[i]:
            if j not in ans:
                ans.append(j)
    return ans

                   
