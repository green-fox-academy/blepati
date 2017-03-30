# Write a recursive function that takes one parameter: n and counts down from n.

def counter(number):
    print(number)
    if number <= 1: #base case
        return 1
    else:
        return number - counter(number-1)

counter(20)
