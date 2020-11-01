def decideNumber(string):
    number = ""
    i = 0
    while i < len(string) and string[i] not in "+-*/^()":
        number = number + str(string[i])
        i += 1
    return [number,i]