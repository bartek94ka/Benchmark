from shutil import *
import shutil
import os
from DiscSpaceInfoProvider import DiscSpaceInfoProvider

class FileTransferManager:
    def copyFile(src, dest):
        directory = os.path.dirname(dest)
        if not os.path.exists(directory):
            os.makedirs(directory)
        try:
            shutil.copy(src, dest)
        # eg. src and dest are the same file
        except shutil.Error as e:
            print('Error: %s' % e)
        # eg. source or destination doesn't exist
        except IOError as e:
            print('Error: %s' % e.strerror)

    def copyLargeFile(src, dest, buffer_size=16000):
        directory = os.path.dirname(dest)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(src, 'rb') as fsrc:
            with open(dest, 'wb') as fdest:
                shutil.copyfileobj(fsrc, fdest, buffer_size)

    def copyFilesFromSpecificDirectory(sourceDirectory, destionationDisc):
        fileList = os.listdir(sourceDirectory)
        statinfo = os.stat(sourceDirectory + '\\File1_.txt')
        fileSize = statinfo.st_size
        fileListSize = len(fileList)
        totalFilesSize = fileListSize * fileSize
        freeSpace = DiscSpaceInfoProvider.getFreeSpace(destionationDisc)
        if(freeSpace < totalFilesSize):
            print("There is not enough memory on destination disc to copy files. Disc name: " + destionationDisc)
            return
        destionationDirectory = destionationDisc + "\\DestinationDirectory"
        for file in fileList:
            srcFilePath = sourceDirectory + "\\" + file
            destFilePath = destionationDirectory + "\\" + file
            FileTransferManager.copyFile(srcFilePath, destFilePath)
        return destionationDirectory