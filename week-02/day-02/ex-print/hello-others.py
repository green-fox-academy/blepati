
def greetMates(names):
    for name in names:
        print ("Hello " + name)

def addMate():
    names = []
    numOfClass = int(input("number of classmates:"))
    for i in range(numOfClass):
        names.append(input())
    return names

print("please, enter the number of your classmates, and then their names")
greetMates(addMate())
