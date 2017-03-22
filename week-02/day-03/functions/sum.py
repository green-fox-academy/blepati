def sum(num):
    if num == 0:
        return 1
    else:
        return num + sum(num - 1)

print(sum(5))
# - Write a function called `sum` that sum all the numbers
#   until the given parameter
