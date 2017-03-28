rev_lines = open("reversed-lines.txt", "r")
new_line = rev_lines.read()

def decrypt(new_file):
    print(new_file[::-1])
    pass

decrypt(new_line)
