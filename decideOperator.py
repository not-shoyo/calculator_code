def decideOperator(opStack,op):
    finalOp = []
    if op == "(":
        opStack.append("(")
        return finalOp,opStack
    elif op == ")":
        insideBracket = opStack.pop()
        while insideBracket != "(":
            finalOp.append(insideBracket)
            insideBracket = opStack.pop()
        return finalOp,opStack
    try:
        prev = opStack.pop()
        if op in "+":
            while prev in "-/*^" and opStack != []:
                finalOp.append(prev)
                prev = opStack.pop()
            else:
                if opStack == []:
                    if prev in "-/*^":
                        finalOp.append(prev)
                    else:
                        opStack.append(prev)
                else:
                    opStack.append(prev)
            opStack.append(op)
        elif op in "-":
            while prev in "/*^" and opStack != []:
                finalOp.append(prev)
                prev = opStack.pop()
            else:
                if opStack == []:
                    if prev in "/*^":
                        finalOp.append(prev)
                    else:
                        opStack.append(prev)
                else:
                    opStack.append(prev)
            opStack.append(op)
        elif op in "/":
            while prev in "*^" and opStack != []:
                finalOp.append(prev)
                prev = opStack.pop()
            else:
                if opStack == []:
                    if prev in "*^":
                        finalOp.append(prev)
                    else:
                        opStack.append(prev)
                else:
                    opStack.append(prev)
            opStack.append(op)
        elif op in "*":
            while prev in "^" and opStack != []:
                finalOp.append(prev)
                prev = opStack.pop()
            else:
                if opStack == []:
                    if prev == "^":
                        finalOp.append(prev)
                    else:
                        opStack.append(prev)
                else:
                    opStack.append(prev)
            opStack.append(op)
        elif op == "^":
            opStack.append(prev)
            opStack.append(op)
    except IndexError:
        opStack.append(op)
    return [finalOp, opStack]