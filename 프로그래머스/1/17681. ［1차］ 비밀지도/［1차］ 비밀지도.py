def solution(n, arr1, arr2):
    ans=[]
    for a,b in zip(arr1,arr2):
        a=bin(a)[2:].rjust(n,"0")
        b=bin(b)[2:].rjust(n,"0")
        print(a,b)
        ret=""
        for i,j in zip(a,b):
            if i=="1" or j=="1":
                ret+="#"
            else:
                ret+=" "
        ans.append(ret)
    return ans
