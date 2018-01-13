import random
import string
import numpy as np
from text_generator import text_generator

class FileGenerator:
    def Generate(size):
        n = 1024 ** 2  # 1 Mb of text
        chars = ''.join([random.choice(string.letters) for i in range(n)])
        f = open('GeneratedFiles/File_' + str(size) + "_MB.txt", "wb")
        f.seek((1048576 - 1) * size)
        f.write(b"\0")
        f.close()

    def GenerateWithText(size):
        letters = np.array(list(chr(ord('a') + i) for i in range(26)))
        n = 1024 ** 2  # 1 Mb of text
        n = n * size
        letter_array = np.random.choice(letters, int(n))
        f = open('GeneratedFiles/File_' + str(size) + "_MB.txt", "w")
        for letter in letter_array:
            f.write(letter)
        f.close()