ans=[]
while True:
    s=input()
    stack=[]
    if s==".":
        break
    balanced=True
    for i in range(len(s)):
        if s[i]=='(' or s[i]=='[':
            stack.append(s[i])
        if s[i]==')':
            if len(stack)==0:
                balanced=False
                break
            last=stack.pop(-1)

            if last!='(':
                balanced=False
                break

        if s[i]==']':
            if len(stack)==0:
                balanced=False
                break
            last=stack.pop(-1)

            if last!='[':
                balanced=False
                break
    if len(stack) !=0:
        balanced=False

    if balanced==True:
        ans.append("yes")
    else:
        ans.append("no")

           

for i in range(len(ans)):
    print(ans[i])
