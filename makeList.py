from decideNumber import decideNumber
from decideOperator import decideOperator

def makeList(inputString = ""):
    myList = []
    myStack = []
    i = 0
    negative = False                                            #################
    
    while i < len(inputString):            
        if inputString[i].isnumeric():
            [number,jump] = decideNumber(inputString[i:])
            if negative is True:                                #################
                myList.append("-"+str(number))                  #################
                negative = False                                #################
            else:                                               #################
                myList.append(number)               
            i += jump
        else:
            OP = inputString[i]
            ops = []                                            #################
            if OP == "-":                                       #################
                if i == 0 or inputString[i-1] == "(":           #################
                    negative = True                             #################
                else:                                           #################
                    [ops, myStack] = decideOperator(myStack,OP) #################
            else:                                               #################
                [ops, myStack] = decideOperator(myStack,OP)
            ops.reverse()
            while ops != []:
                myList.append(ops.pop())   
            i += 1
    if myStack != []:
        while myStack != []:
            last = myStack.pop()
            if last != "(":
                myList.append(last)
    return myList