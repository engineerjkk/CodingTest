def solution(s):
    answer = 0
    n=len(s)
    min_length=n
    for i in range(1,n//2+1):
        compressed=[]
        prev=s[:i]
        cnt=1
        for j in range(i,n,i):
            current=s[j:j+i]
            if prev==current:
                cnt+=1
            else:
                if cnt>1:
                    compressed.append(f"{cnt}{prev}")
                else:
                    compressed.append(prev)
                cnt=1
                prev=current
        if cnt>1:
            compressed.append(f"{cnt}{prev}")
        else:
            compressed.append(prev)
        min_length=min(min_length,len("".join(compressed)))
    return min_length