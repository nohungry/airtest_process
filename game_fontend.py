from airtest.core.api import *
from airtest.core.api import G
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import connect_device
from airtest.core.settings import Settings as ST
from airtest.aircv.keypoint_matching_contrib import SIFTMatching

import time

# 手機連接使用
# 儲存在G_Class全域裡面
device1 = connect_device("Android:///1576457605007R5?cap_method=minicap&touch_method=adb")

# ----------------------------------------------------------------------
# screenshot 可使用
# screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)

# ----------------------------------------------------------------------
# 設定圖像辨識的方法為特徵點匹配
ST.CVSTRATEGY = ["sift"]
# set timeout
ST.FIND_TIMEOUT = 100

# ----------------------------------------------------------------------
# MATCHING_METHOD
MATCHING_METHODS = {
    "sift": SIFTMatching
}
func = MATCHING_METHODS.get("sift", None)

# ----------------------------------------------------------------------
# windows screen 預處理完成, 轉變為CV2格式
windowsScreen = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_screen\windows_screen.jpg")
screenCV2 = windowsScreen._imread()

# ----------------------------------------------------------------------
targetSpin = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\windows_spin.jpg")

# ----------------------------------------------------------------------
# match_in process
# _cv_match process
# _try_match process
ret = SIFTMatching(targetSpin, screenCV2)
ret.find_best_result()