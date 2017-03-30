rev_order = open("reversed_order.txt", "r")
new_order = rev_order.readlines()

def decrypt(new_file):
    print(new_order[::-1])

decrypt(new_order)

#almost there
