from shutil import *
import shutil
import os

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