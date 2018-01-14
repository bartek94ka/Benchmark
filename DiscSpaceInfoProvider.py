import shutil
import os

class DiscSpaceInfoProvider():

    def getFreeSpace():
        freeSpace = shutil.disk_usage(os.getcwd()).free
        return freeSpace

    def getFreeSpace(disc):
        freeSpace = shutil.disk_usage(disc + "\\").free
        return freeSpace