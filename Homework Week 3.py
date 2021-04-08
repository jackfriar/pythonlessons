def SumWhile(arg0=0):
    i = arg0
    y = 0
    while i <= 100:
        y += i
        i += 1
    return y

def SumRange(arg0=0):
    y = 0
    for x in range(arg0, 101):
        y += x
    return y

def Main():
    print("\nThis program outputs the sum of the numbers from n to 100")
    sum = input("Please enter the value of n: ")
    print("\nDo you want to compute the result using While cycles or Ranges?")
    mode = input("Choose [w/r]: ")
    if mode == "w":
        print("\nThe sum is:", SumWhile(int(sum)))
    elif mode == "r":
        print("\nThe sum is:", SumRange(int(sum)))
    else:
        print("There was an error. Start Over\n\n")
        Main()

Main()
