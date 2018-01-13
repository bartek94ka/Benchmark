import random
import string
import numpy as np
import os
from FileTransferManager import FileTransferManager

class FileGenerator:
    def Generate(size):
        n = 1024 ** 2  # 1 Mb of text
        chars = ''.join([random.choice(string.letters) for i in range(n)])
        f = open('GeneratedFiles/File_' + str(size) + "_MB.txt", "wb")
        f.seek((1048576 - 1) * size)
        f.write(b"\0")
        f.close()

    def GenerateWithText2(directory, fileName, size):
        letters = np.array(list(chr(ord('a') + i) for i in range(26)))
        n = 1024 ** 2  # 1 Mb of text
        n = n * size
        letter_array = np.random.choice(letters, int(n))
        f = open('GeneratedFiles/File_' + str(size) + "_MB.txt", "w")
        for letter in letter_array:
            f.write(letter)
        f.close()

    def GenerateWithText(directory, fileName, size):
        filePath = directory + "\\" + fileName + ".txt"
        letters = np.array(list(chr(ord('a') + i) for i in range(26)))
        n = 1024 ** 2  # 1 Mb of text
        n = n * size
        letter_array = np.random.choice(letters, int(n))
        f = open(filePath, "w")
        for letter in letter_array:
            f.write(letter)
        f.close()

    def GenerateTestFiles(disc, quantity, size):
        directory = disc + ":\\GeneratedFiles\\Quantity_" + str(quantity) + "_Size_" + str(size) + "_MB"
        if not os.path.exists(directory):
            os.makedirs(directory)
        fileName = "File1_"
        FileGenerator.GenerateWithText(directory, fileName, size)
        sourceFilePath = directory + "\\" + fileName + ".txt"
        for i in range(2,quantity + 1, 1):
            destFileName = "File" + str(i) + "_"
            destFilePath = directory + "\\" + destFileName + ".txt"
            FileTransferManager.copyFile(sourceFilePath, destFilePath)
        return directory