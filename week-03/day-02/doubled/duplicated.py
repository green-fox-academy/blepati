duplicated = open("duplicated-chars.txt")
#print(duplicated.read())
letters = duplicated.read()

def decrypt(new_file):
    ll = len(new_file)
    print(new_file[0:ll:2])

decrypt(letters)
#minden paratlan betut printeljen ki (valami%2 == 1)
#duplicated.close()
