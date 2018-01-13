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
    FileTransferManager.copyLargeFile(sourceFile, destinationPath)
    end = time.time()
    print(end - start)


def MeasureFileTransferOperation(sourceFilePath, destinationPath):
    start = time.time()
    destinationPath = destinationPath + os.path.basename(sourceFilePath)
    FileTransferManager.copyFile(sourceFilePath, destinationPath)
    end = time.time()
    duration = end - start
    return duration

def MeasureFileTransferOpertaionTest():
    sourceFile = os.getcwd() + '\\GeneratedFiles\\File_1_MB.txt'
    destinationPath = 'E:\\'
    time = MeasureFileTransferOperation(sourceFile, destinationPath)
    print(time)

def GenerateTestFileCollection():
    #parametr: litera dysku, ilość plików, wielkość danych w MB
    #zwraca ścieżke do lokalizacji, gdzie pliki zostały stworzone
    createdFilesDirectory = FileGenerator.GenerateTestFiles('D', 3, 3)

def main():
    #FileGenerator.Generate(100)
    #FileGenerator.GenerateWithText(1.5)
    #CSVManagerTest()
    #FileTransferManagerTest()
    # MeasureFileTransferOpertaionTest()
    GenerateTestFileCollection()

if __name__ == "__main__":
    main()