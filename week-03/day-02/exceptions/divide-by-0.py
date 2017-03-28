num = input("Please, write in a number: ")
divider = 10

try:
    z = divider / int(num)
    print(z)
except ZeroDivisionError:
    print("fail")


# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0
