from itertools import permutations

def operation(num1,num2,o):
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
                stack.append(operation(stack.pop(),array.pop(0),o))
            else:
                stack.append(tmp)
        array=stack
    return abs(int(array[0]))
    
def solution(expression):
    answer=[]
    oper=['+','-','*']
    oper=permutations(oper,3)
    for i in oper:
        answer.append(calculate(i,expression))
    return max(answer)