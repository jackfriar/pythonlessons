def MaxRecursion(arglist, argi):
    if argi == 1:
        return arglist[argi-1]
    else:
        i = MaxRecursion(arglist, argi-1)
        j = arglist[argi-1]
        if i > j: 
            return i
        else: 
            return j

def Max(arglist):
    maxn = 0
    for x in arglist:
        if x >= maxn:
            maxn = x
    return maxn

def AskForNumbers():
    numbers = []
    while(True):
        loc = input("Insert a number or 'e' to exit: ")
        if loc == "e":
            break
        else:
            numbers.append(int(loc))
    return numbers

numbers = AskForNumbers()
print("The maximum number using recursion is:", MaxRecursion(numbers, len(numbers)))
print("The maximum number using cycles is: ", Max(numbers))