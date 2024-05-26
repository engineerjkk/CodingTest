def solution(n, arr1, arr2):
    answer = []
    bin_arr1=[]
    bin_arr2=[]
    for i in arr1:
        a=str(bin(i))[2:]
        b=""
        if len(a)<n:
            for _ in range(n-len(a)):
                b+="0"
        bin_arr1.append(b+a)
    for i in arr2:
        a=str(bin(i))[2:]
        b=""
        if len(a)<n:
            for _ in range(n-len(a)):
                b+="0"
        bin_arr2.append(b+a)
    space=[]
    for i in range(n):
        tmp=""
        for j in range(n):
            if bin_arr1[i][j]=="1" or bin_arr2[i][j]=="1":
                tmp+="#"
            else:
                tmp+=" "
        space.append(tmp)

        

    return space