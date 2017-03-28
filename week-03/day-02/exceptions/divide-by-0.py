def kacsa(num):
    divider = 10
    try:
        z = divider / num
        print(z)
    except ZeroDivisionError:
        print("fail")

kacsa(0)

# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0
