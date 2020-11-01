from makeList import makeList
from evaluate import evaluate 

valid = {"1","2","3","4","5","6","7","8","9","0","+","-","*","/","^","(",")"}

def mainFunction(expression = ""):
    if valid.issuperset(expression):
        return evaluate(makeList(expression))
    else:
        return "Invalid input"

