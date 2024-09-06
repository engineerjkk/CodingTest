from itertools import permutations
def solution(expression):
    
    def operations(num1,num2,o):
        if o=='+':
            return str(int(num1)+int(num2))
        if o=='-':
            return str(int(num1)-int(num2))
        if o=='*':
            return str(int(num1)*int(num2))
    
    def calculate(op,exp):
        tmp=''
        array=[]
        for i in exp:
            if i.isdigit():
                tmp+=i
            else:
                array.append(tmp)
                array.append(i)
                tmp=''
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
    
    answer = 0
    operation=['+','-','*']
    for op in list(permutations(operation,3)):
        answer=max(answer,calculate(op,expression))
    return answer