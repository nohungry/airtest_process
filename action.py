import os
import common

from datetime import datetime
from airtest.core.api import *
from airtest.core.api import G
from airtest.core.api import connect_device
from airtest.core.settings import Settings as ST

# def deviceConnect(uuid=None):
#     if uuid == None:
#         uuid = "1576457605007R5"
#     device = connect_device("Android:///%s?cap_method=minicap&touch_method=adb" % (uuid))
    
#     return device

def deviceConnect(uuid=None):
    if uuid == None:
        uuid = "1576457605007R5"
    device = connect_device("Android://127.0.0.1:5037/%s?cap_method=minicap&touch_method=adb" % (uuid))

    return device

def deviceRemoteConnect(ip=None):
    if ip == None:
        ip = "10.200.8.110:5555"
    device = connect_device("Android:///%s?cap_method=minicap&touch_method=adb" % (ip))

    return device

def phoneResolution():
    phone_resolution = {}
    phone_resolution["height"] = G.DEVICE.display_info["height"]
    phone_resolution["width"] = G.DEVICE.display_info["width"]

    return phone_resolution

def parseImage(path):
    # path: .jpg file
    # 同時套上airtest.core.api class Template
    template = Template(path)
    parseCV2 = template._imread()

    return parseCV2

def phoneSnapShot(device, path):
    nowTime = datetime.today().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(path, r"screen_" + nowTime + ".jpg")
    snapshot = device.snapshot(filename=filename, quality=ST.SNAPSHOT_QUALITY)
    imageCV2 = parseImage(filename)
    
    return imageCV2