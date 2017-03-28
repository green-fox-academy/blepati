duplicated = open("duplicated-chars.txt")
#print(duplicated.read())
letters = duplicated.read()
ll = len(letters)

print(letters[0:ll:2])


#minden paratlan betut printeljen ki (valami%2 == 1)
#duplicated.close()
