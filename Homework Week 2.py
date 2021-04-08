def start():

    legalage = 18
    print("My friend and I go to a bar")
    ageStr = input("Tell me your age: ")
    age = int(ageStr)

    if age >= legalage:
        if age in range(legalage, legalage + 2):
            print("Give me your ID: ")
            input("Name: ")
            ageDeclaredStr = input("Age: ")
            ageDeclared = int(ageDeclaredStr)
            if ageDeclared >= legalage:
                print("Okay, here is your drink")
            else:
                print("Go away")
        elif age not in range(legalage + 3):
            print("Okay, here is your drink")
    else:
        print("Go away")
    pass

def mainMenu():
    print("Hello, player. Would you like to start?")
    x = input("(start/quit): ")
    if x == "start":
        start()
    elif x == "quit":
        quit()
    else:
        mainMenu()

mainMenu()
