t=int(input())
for _ in range(t):
    m,n,x,y=map(int,input().split())

    if m<n:
        m,n=n,m
        x,y=y,x
    found=False
    first=y
    for i in range(m):
        if first==x:
            print(y+i*n)
            found=True
            break
        first+=n
        if first>m:
            first-=m
    
    if not found:
        print(-1)
