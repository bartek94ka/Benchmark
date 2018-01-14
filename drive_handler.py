
import win32con
from win32api import *
from win32file import GetDriveType
import shutil


def get_drives_list(drive_types=(win32con.DRIVE_REMOVABLE,)):
    ret = list()
    ret.append("none")
    drives_str = GetLogicalDriveStrings()
    drives = [item for item in drives_str.split("\x00") if item]
    for drive in drives:
        if GetDriveType(drive) in drive_types:
            ret.append(drive[:2])
    return ret


def get_drive_info(drive):
    ret = ""
    try:
        ret += GetVolumeInformation(drive)[0]
    except:
        ret = ""

    return ret


def get_transfer_speed(drive):
    ret = 0
    try:
        s = GetDiskFreeSpace(drive)
        ret = s[0]*s[1]*s[2]
    except:
        ret = 0

    return ret

