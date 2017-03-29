duplicated = open("duplicated-chars.txt")

letters = duplicated.read()

def decrypt(new_file):
    ll = len(new_file)
    print(new_file[0:ll:2])

decrypt(letters)

duplicated.close()
