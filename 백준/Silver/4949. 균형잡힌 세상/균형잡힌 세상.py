ans=[]
while True:
    lst=[]
    s=input()
    balanced=True
    if s==".":
        break
    for i in range(len(s)):
        if s[i]=='(' or s[i]=='[':
            lst.append(s[i])
        
        if s[i]==')':
            if len(lst)==0:
                balanced=False
                break
            last=lst.pop(-1)
            if last!='(':
                balanced=False
                break

        if s[i]==']':
            if len(lst)==0:
                balanced=False
                break
            last=lst.pop(-1)
            if last!='[':
                balanced=False
                break
    if len(lst)!=0:
        balanced=False
    if balanced==True:
        ans.append("yes")
    else:
        ans.append("no")
for i in range(len(ans)):
    print(ans[i])