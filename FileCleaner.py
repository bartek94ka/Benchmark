import os

class FileCleaner():
    def RemoveFilesFromDirectory(directory):
        fileList = os.listdir(directory)
        for file in fileList:
            filePath = directory + "\\" + file
            os.remove(filePath)

    def RemoveDirectory(directory):
        os.rmdir(directory)

    def RemoveDirectoryWithFiles(directory):
        FileCleaner.RemoveFilesFromDirectory(directory)
        FileCleaner.RemoveDirectory(directory)