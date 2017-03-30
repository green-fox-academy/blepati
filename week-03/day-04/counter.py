# Write a recursive function that takes one parameter: n and counts down from n.

def counter(number):
    print(number)
    if number == 0: #base case
        return 0
    else:
        return number - counter(number-1)

counter(20)
