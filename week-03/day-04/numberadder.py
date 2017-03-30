# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def summary(number):
    if number <= 1: #base case
        return 1
    else:
        return number + summary(number-1)

print(summary(9))
