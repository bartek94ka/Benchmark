import shutil
import os

class DiscSpaceInfoProvider():
    def getFreeSpace():
        freeSpace = shutil.disk_usage(os.getcwd()).free
        return freeSpace