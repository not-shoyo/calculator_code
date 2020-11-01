from operate import operate

stack = []

def evaluate(myList = []):
    myList.reverse()
    while myList != []:
        a = myList.pop()
        if a in "+-*/^":
            op = a
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(operate(num1,num2,op))
        else:
            stack.append(int(a))
    return stack[0]
                    
        