from ast import While
from turtle import position
from airtest.core.api import *
from airtest.core.api import G
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import connect_device
from airtest.core.settings import Settings as ST
from airtest.aircv.keypoint_matching_contrib import SIFTMatching
from airtest.utils.transform import TargetPos

from feature_Re import KAZEMatching
import time

real_position = {
    'spin': (536, 2066),
    'addition': (772, 1905),
    'subtraction': [299, 1904],
    'lighting': (917, 2038),
    'loop': (176, 2022),
    'contents': (994, 1876),
    'lobby': (111, 1946),
    'record': (322, 1950),
    'rule': (539, 1942),
    'musicSetting': (757, 1945),
    'cancel': [965, 1903]
}

# 手機連接使用
# 儲存在G_Class全域裡面
device1 = connect_device("Android:///1576457605007R5?cap_method=minicap&touch_method=adb")

# ----------------------------------------------------------------------
# screenshot 可使用
# screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
# snapshot = Template(screen)
# screenCV2 = snapshot._imread()

# ----------------------------------------------------------------------
# 設定圖像辨識的方法為特徵點匹配
# ST.CVSTRATEGY = ["sift"]
# set timeout
# ST.FIND_TIMEOUT = 100

# ----------------------------------------------------------------------
# MATCHING_METHOD
# MATCHING_METHODS = {
#     "sift": SIFTMatching
# }
# func = MATCHING_METHODS.get("sift", None)

# ----------------------------------------------------------------------
# windows screen 預處理完成, 轉變為CV2格式
windowsScreen = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_screen\windows_screen.jpg")
screenCV2 = windowsScreen._imread()

# ----------------------------------------------------------------------
# targetSpin = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\windows_spin.jpg")
# targetCV2 = targetSpin._imread()

# ----------------------------------------------------------------------
# match_in process
# _cv_match process
# _try_match process
# match_result = None
# while match_result is True:
# for _ in range(10):
#     ret = SIFTMatching(targetCV2, screenCV2)
#     match_result = ret.find_best_result()
#     time.sleep(2)
# pass

# ----------------------------------------------------------------------
# record pos
touchPos = {}

# ----------------------------------------------------------------------
# step01. spin
for _ in range(10):
    # screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
    # snapshot = Template(screen)
    # screenCV2 = snapshot._imread()

    targetSpin = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\windows_spin.jpg")
    targetCV2 = targetSpin._imread()

    ret = SIFTMatching(targetCV2, screenCV2, threshold=0.5)
    ret1 = KAZEMatching(targetCV2, screenCV2, threshold=0.5)
    match_result = ret.find_best_result()
    test = ret1.find_best_result()
    if match_result != None:
        break
    time.sleep(2)

# pos = TargetPos().getXY(match_result, 5)
# G.DEVICE.touch(pos)
# touchPos["spin"] = pos
# time.sleep(30)

# # ----------------------------------------------------------------------
# # step02. addition
# for _ in range(10):
#     screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
#     snapshot = Template(screen)
#     screenCV2 = snapshot._imread()

#     targetSpin = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\addition.jpg")
#     targetCV2 = targetSpin._imread()

#     ret = SIFTMatching(targetCV2, screenCV2, threshold=0.5)
#     match_result = ret.find_best_result()
#     if match_result != None:
#         break
#     time.sleep(2)

# pos = TargetPos().getXY(match_result, 5)
# G.DEVICE.touch(pos)
# touchPos["addition"] = pos
# time.sleep(5)

# # ----------------------------------------------------------------------
# # step03. subtraction
# for _ in range(10):
#     screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
#     snapshot = Template(screen)
#     screenCV2 = snapshot._imread()

#     targetSpin = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\subtraction.jpg")
#     targetCV2 = targetSpin._imread()

#     ret = SIFTMatching(targetCV2, screenCV2, threshold=0.5)
#     match_result = ret.find_best_result()
#     if match_result != None:
#         break
#     time.sleep(2)

# pos = TargetPos().getXY(match_result, 5)
# G.DEVICE.touch(pos)
# touchPos["subtraction"] = pos
# time.sleep(5)

# # ----------------------------------------------------------------------
# # step04. lighting
# for _ in range(10):
#     screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
#     snapshot = Template(screen)
#     screenCV2 = snapshot._imread()

#     targetSpin = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\lighting.jpg")
#     targetCV2 = targetSpin._imread()

#     ret = SIFTMatching(targetCV2, screenCV2, threshold=0.5)
#     match_result = ret.find_best_result()
#     if match_result != None:
#         break
#     time.sleep(2)

# pos = TargetPos().getXY(match_result, 5)
# G.DEVICE.touch(pos)
# time.sleep(5)
# G.DEVICE.touch(pos)
# touchPos["lighting"] = pos
# time.sleep(5)

# # ----------------------------------------------------------------------
# # step05. loop
# for _ in range(10):
#     screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
#     snapshot = Template(screen)
#     screenCV2 = snapshot._imread()

#     targetSpin = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\loop.jpg")
#     targetCV2 = targetSpin._imread()

#     ret = SIFTMatching(targetCV2, screenCV2, threshold=0.5)
#     match_result = ret.find_best_result()
#     if match_result != None:
#         break
#     time.sleep(2)

# pos = TargetPos().getXY(match_result, 5)
# touchPos["loop"] = pos
# time.sleep(5)

# # ----------------------------------------------------------------------
# # step06. contents
# for _ in range(10):
#     screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
#     snapshot = Template(screen)
#     screenCV2 = snapshot._imread()

#     targetSpin = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\contents.jpg")
#     targetCV2 = targetSpin._imread()

#     ret = SIFTMatching(targetCV2, screenCV2, threshold=0.5)
#     match_result = ret.find_best_result()
#     if match_result != None:
#         break
#     time.sleep(2)

# pos = TargetPos().getXY(match_result, 5)
# G.DEVICE.touch(pos)
# touchPos["contents"] = pos
# time.sleep(5)

# # ----------------------------------------------------------------------
# # step07. contents inside lobby
# for _ in range(10):
#     screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
#     snapshot = Template(screen)
#     screenCV2 = snapshot._imread()

#     targetSpin = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\lobby.jpg")
#     targetCV2 = targetSpin._imread()

#     ret = SIFTMatching(targetCV2, screenCV2, threshold=0.5)
#     match_result = ret.find_best_result()
#     if match_result != None:
#         break
#     time.sleep(2)

# pos = TargetPos().getXY(match_result, 5)
# touchPos["lobby"] = pos
# time.sleep(5)

# # ----------------------------------------------------------------------
# # step08. contents inside record
# for _ in range(10):
#     screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
#     snapshot = Template(screen)
#     screenCV2 = snapshot._imread()

#     targetSpin = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\record.jpg")
#     targetCV2 = targetSpin._imread()

#     ret = SIFTMatching(targetCV2, screenCV2, threshold=0.5)
#     match_result = ret.find_best_result()
#     if match_result != None:
#         break
#     time.sleep(2)

# pos = TargetPos().getXY(match_result, 5)
# touchPos["record"] = pos
# time.sleep(5)

# # ----------------------------------------------------------------------
# # step09. contents inside rule
# for _ in range(10):
#     screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
#     snapshot = Template(screen)
#     screenCV2 = snapshot._imread()

#     targetSpin = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\rule.jpg")
#     targetCV2 = targetSpin._imread()

#     ret = SIFTMatching(targetCV2, screenCV2, threshold=0.5)
#     match_result = ret.find_best_result()
#     if match_result != None:
#         break
#     time.sleep(2)

# pos = TargetPos().getXY(match_result, 5)
# touchPos["rule"] = pos
# time.sleep(5)

# # ----------------------------------------------------------------------
# # step10. contents inside music setting
# for _ in range(10):
#     screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
#     snapshot = Template(screen)
#     screenCV2 = snapshot._imread()

#     targetSpin = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\musicSetting.jpg")
#     targetCV2 = targetSpin._imread()

#     ret = SIFTMatching(targetCV2, screenCV2, threshold=0.5)
#     match_result = ret.find_best_result()
#     if match_result != None:
#         break
#     time.sleep(2)

# pos = TargetPos().getXY(match_result, 5)
# touchPos["musicSetting"] = pos
# time.sleep(5)

# # ----------------------------------------------------------------------
# # step11. contents inside cancel
# for _ in range(10):
#     screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
#     snapshot = Template(screen)
#     screenCV2 = snapshot._imread()

#     targetSpin = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\contents_cancel.jpg")
#     targetCV2 = targetSpin._imread()

#     ret = SIFTMatching(targetCV2, screenCV2, threshold=0.5)
#     match_result = ret.find_best_result()
#     if match_result != None:
#         break
#     time.sleep(2)

# pos = TargetPos().getXY(match_result, 5)
# G.DEVICE.touch(pos)
# touchPos["cancel"] = pos
# time.sleep(5)

print(touchPos)
pass