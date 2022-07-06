import os

from airtest.core.api import *
from airtest.core.api import G
from airtest.core.api import connect_device
from pip import main
from airtest.core.settings import Settings as ST
# from airtest.utils.transform import TargetPos

from feature_Re import KAZEMatching

DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop") + "\\"

def deviceConnect(uuid=None):
    if uuid == None:
        uuid = "1576457605007R5"
    device = connect_device("Android:///%s?cap_method=minicap&touch_method=adb" % (uuid))
    
    return device


def parseImage(path):
    # path: .jpg file
    template = Template(path)
    parseCV2 = template._imread()

    return parseCV2

def phoneSnapShot(device):
    screenFolderPath = os.path.join(DESKTOP, r"")
    snapshot = device.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
    imageCV2 = parseImage(snapshot)
    
    return imageCV2


if __name__ == '__main__':
    android_phone = deviceConnect()
    imageCV2 = phoneSnapShot(android_phone)
    pass