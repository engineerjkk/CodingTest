from itertools import permutations

def operations(num1,num2,o):
    if o=='+':
        return str(int(num1)+int(num2))
    if o=='-':
        return str(int(num1)-int(num2))
    if o=='*':
        return str(int(num1)*int(num2))

def calculate(op,exp):
    tmp=""
    array=[]
    for i in exp:
        if i.isdigit()==True:
            tmp+=i
        else:
            array.append(tmp)
            array.append(i)
            tmp=""
    array.append(tmp)

    for o in op:
        stack=[]
        while len(array)!=0:
            tmp=array.pop(0)
            if tmp==o:
                stack.append(operations(stack.pop(),array.pop(0),o))
            else:
                stack.append(tmp)
        array=stack
    return abs(int(array[0]))
def solution(expression):
    answer = 0
    oper=['+','-','*']
    lst=permutations(oper,3)
    result=[]
    for i in lst:
        result.append(calculate(i,expression))
    return max(result)