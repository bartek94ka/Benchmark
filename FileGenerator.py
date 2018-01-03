class FileGenerator:
    def Generate(size):
        f = open('GeneratedFiles/newfile', "wb")
        f.seek((1048576 - 1) * size)
        f.write(b"\0")
        f.close()