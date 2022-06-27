from fileinput import filename
from airtest.core.api import *
from airtest.core.api import G
# from airtest.cli.parser import cli_setup
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import connect_device
from airtest.core.settings import Settings as ST
import numpy as np
import cv2
import os

device1 = connect_device("Android:///1576457605007R5?cap_method=minicap&touch_method=adb")
print(G.DEVICE_LIST)
# deviceInfo = device()

# {'width': 1080, 'height': 2400, 'density': 3.0, 'orientation': 0, 'rotation': 0, 'max_x': 1619, 'max_y': 3599}

# 網頁遊戲端_SLOT
# touch(Template(r"C:\Users\norman_cheng\Desktop\airtest_project\test001.air\roll.png", record_pos=(-0.003, 0.703), resolution=(1080, 2400)))
a = Template(r"C:\Users\norman_cheng\Desktop\airtest_project\test001.air\roll.png")
touch(a)
# desktop = os.path.join(os.path.expanduser("~"), "Desktop") + "\\"
# filepath = os.path.join(desktop, r"log_use001")
# bb = r"C:\Users\norman_cheng\Desktop\airtest_project\test001.air\roll.png"

# test = np.fromfile(bb, dtype=np.uint8)
# decode = cv2.imdecode(test, cv2.IMREAD_COLOR)


# arrayText = os.path.join(filepath, r"test.txt")
# f = open(arrayText, "w")
# for index in test:
#     f.write(index)
#     f.write("\r\n")
# f.close()

# screenshot 可使用
screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)


