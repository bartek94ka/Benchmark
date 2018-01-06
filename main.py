from FileGenerator import FileGenerator
from CSVManager import CSVManager
from FileTransferManager import FileTransferManager
import os
import time

def CSVManagerTest():
    CSVManager.WriteData('C:\CSVTest', 'test1.csv', ['a', 'b', 'c'])
    data1 = CSVManager.ReadData('C:\CSVTest/test1.csv')
    print(data1)
    dictData = [{'time': 'a', 'datatransferred': 'b'},
                {'time': 'c', 'datatransferred': 'd'},
                {'time': 'e', 'datatransferred': 'f'}]
    CSVManager.WriteDictionaryData('C:\CSVTest', 'test2.csv', dictData)
    data2 = CSVManager.ReadDictionaryData('C:\CSVTest/test2.csv')
    print(data2)

def FileTransferManagerTest():
    sourceFile = os.getcwd() + '\\GeneratedFiles\\File_1_MB.txt'
    destinationPath = os.getcwd() + '\\TransferedFiles\\File_1_MB.txt'

    start = time.time()
    #FileTransferManager.copyFile(sourceFile, destinationPath)
    #FileTransferManager.copyLargeFile(sourceFile, destinationPath)
    end = time.time()
    print(end - start)


def main():
    #FileGenerator.Generate(1)
    #CSVManagerTest()
    FileTransferManagerTest()

if __name__ == "__main__":
    main()