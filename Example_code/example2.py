with open("file.txt", "r") as in_file:
    buf = in_file.readlines()
    
with open("file.txt", "w") as out_file:
    for line in buf:
        if line == " Include this text\n":
            line = line + "Include below\n"
            out_file.write(line)