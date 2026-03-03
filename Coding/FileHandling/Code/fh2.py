# File is closed automatically

with open("./FileHandling/Files/myfile2.txt", "w") as fobj:
    fobj.write("Hello! I am here!!!")
    
with open("./FileHandling/Code/fh1.py", "r") as fobj:
    content = fobj.read()
    print(content)
