def factorio(num):
    if num == 0:
        return 1
    else:
        return num * factorio(num - 1)

print(factorio(6))

# - Create a function called `factorio`
#   that returns it's input's factorial
