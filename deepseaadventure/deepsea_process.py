import os
import sys
from turtle import position

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

import action
import procedures
import time

from airtest.utils.transform import TargetPos

from feature_Re import KAZEMatching

DIR_NAME = os.path.dirname(__file__)
# TARGET_DIR = os.path.join(DIR_NAME, r"deepsea_target")
TARGET_DIR = os.path.join(DIR_NAME, r"deepsea_target2")

# TEMP = {
#     "spin": os.path.join(TARGET_DIR, r"spin.jpg"),
#     "addition": os.path.join(TARGET_DIR, r"addition.jpg"),
#     # -----------------------------------------------------------
#     "subtraction": os.path.join(TARGET_DIR, r"subtraction.jpg"),
#     "subtraction01": os.path.join(TARGET_DIR, r"subtraction01.jpg"),
#     "subtraction02": os.path.join(TARGET_DIR, r"subtraction02.jpg"),
#     # -----------------------------------------------------------
#     "lighting": os.path.join(TARGET_DIR, r"lighting.jpg"),
#     "loop": os.path.join(TARGET_DIR, r"loop.jpg"),
#     "autoloop": os.path.join(TARGET_DIR, r"autoloop.jpg"),
#     "autostart": os.path.join(TARGET_DIR, r"autostart.jpg"),
#     "autocancel": os.path.join(TARGET_DIR, r"autocancel.jpg"),
#     "contents": os.path.join(TARGET_DIR, r"contents.jpg"),
#     "lobby": os.path.join(TARGET_DIR, r"lobby.jpg"),
#     "record": os.path.join(TARGET_DIR, r"record.jpg"),
#     "recordcancel": os.path.join(TARGET_DIR, r"recordcancel.jpg"),
#     "rule": os.path.join(TARGET_DIR, r"rule.jpg"),
#     "ruleswitch": os.path.join(TARGET_DIR, r"ruleswitch.jpg"),
#     "rulecancel": os.path.join(TARGET_DIR, r"rulecancel.jpg"),
#     "musicsetting": os.path.join(TARGET_DIR, r"musicSetting.jpg"),
#     "settingcancel": os.path.join(TARGET_DIR, r"settingcancel.jpg"),
#     "cancel": os.path.join(TARGET_DIR, r"contents_cancel.jpg"),
#     "popoutalert": os.path.join(TARGET_DIR, r"popout.jpg"),
#     "confirm": os.path.join(TARGET_DIR, r"confirm.jpg"),
# }

TEMP = {
    "spin": os.path.join(TARGET_DIR, r"spin.png"),
    "addition": os.path.join(TARGET_DIR, r"addition.png"),
    # -----------------------------------------------------------
    "subtraction": os.path.join(TARGET_DIR, r"subtraction.png"),
    # -----------------------------------------------------------
    "lighting": os.path.join(TARGET_DIR, r"lighting.png"),
    "loop": os.path.join(TARGET_DIR, r"loop.png"),
    "autoloop": os.path.join(TARGET_DIR, r"autoloop.jpg"),
    "autostart": os.path.join(TARGET_DIR, r"autostart_word.png"),
    "autocancel": os.path.join(TARGET_DIR, r"autocancel.png"),
    "contents": os.path.join(TARGET_DIR, r"contents.png"),
    "lobby": os.path.join(TARGET_DIR, r"lobby.png"),
    "record": os.path.join(TARGET_DIR, r"record.png"),
    "recordcancel": os.path.join(TARGET_DIR, r"recordcancel.jpg"),
    "rule": os.path.join(TARGET_DIR, r"rule.png"),
    "ruleswitch": os.path.join(TARGET_DIR, r"ruleswitch.png"),
    "rulecancel": os.path.join(TARGET_DIR, r"rulecancel.png"),
    "musicsetting": os.path.join(TARGET_DIR, r"musicSetting.png"),
    "settingcancel": os.path.join(TARGET_DIR, r"settingcancel.png"),
    "cancel": os.path.join(TARGET_DIR, r"contents_cancel.png"),
    "popoutalert": os.path.join(TARGET_DIR, r"popout_message.png"),
    "confirm": os.path.join(TARGET_DIR, r"confirm_word.png"),
}

class deepseaImagePos(procedures.procedures):
    def universal(self, device, path, sign=None, touch=True):
        # device: Phone
        # path: snapshot download folder path
        for _ in range(3):
            snapshotCV2 = action.phoneSnapShot(device, path)
            if sign == None:
                raise EOFError("sign參數請參照TEMP使用")
            targetCV2 = action.parseImage(sign)
            match_result = KAZEMatching(targetCV2, snapshotCV2, threshold=0.5).find_best_result()
            if match_result != None:
                break
            time.sleep(2)
        if touch == True:
            if match_result != None:
                position = TargetPos().getXY(match_result, 5)
                device.touch(position)
                time.sleep(10)
                match_result["result"] = ", ".join(map(str, match_result["result"]))
                return match_result

            elif match_result == None:
                errortarget = os.path.basename(sign)
                print("手機當前頁面上沒有找到正確的圖片_%s" %errortarget)
                none_result = {
                    "result": None,
                    "rectangle": None,
                    "confidence": None,
                    "time": None
                }
                return none_result
        elif touch == False:
            if match_result != None:
                position = TargetPos().getXY(match_result, 5)
                match_result["result"] = ", ".join(map(str, match_result["result"]))
                return match_result

            elif match_result == None:
                errortarget = os.path.basename(sign)
                print("手機當前頁面上沒有找到正確的圖片_%s" %errortarget)
                none_result = {
                    "result": None,
                    "rectangle": None,
                    "confidence": None,
                    "time": None
                }
                return none_result

def deepseaFlow(device, path):
    # position record
    pos = {}

    # 旋轉
    spinPosition = deepseaImagePos().universal(device, path, TEMP["spin"])
    pos["spin"] = spinPosition

    # 金額"+"
    additionPosition = deepseaImagePos().universal(device, path, TEMP["addition"])
    pos["addition"] = additionPosition

    # 金額"-"
    subtractionPosition = deepseaImagePos().universal(device, path, TEMP["subtraction"])
    pos["subtraction"] = subtractionPosition

    # 快速按鈕(highlight)
    lightingPosition = deepseaImagePos().universal(device, path, TEMP["lighting"])
    pos["lighting"] = lightingPosition

    # # 取消快速按鈕(no highlight)
    # lightingPosition = deepseaImagePos().universal(device, path, TEMP["lighting"])

    # 循環按鈕
    loopPosition = deepseaImagePos().universal(device, path, TEMP["loop"])
    pos["loop"] = loopPosition

    # 循環設定頁
    autoloopPosition = deepseaImagePos().universal(device, path, TEMP["autoloop"], touch=False)
    pos["autoloop"] = autoloopPosition

    # 循環開始
    autostartPosition = deepseaImagePos().universal(device, path, TEMP["autostart"])
    pos["autostart"] = autostartPosition
    print("# --------------------------")
    print("等候120秒")
    print("# --------------------------")
    time.sleep(120)

    # # 循環設定頁_取消
    # autocancelPosition = deepseaImagePos().universal(device, path, TEMP["autocancel"])
    # pos["autocancel"] = autocancelPosition

    # 目錄按鈕
    contentsPosition = deepseaImagePos().universal(device, path, TEMP["contents"])
    pos["contents"] = contentsPosition

    # 返回KK大廳
    lobbyPosition = deepseaImagePos().universal(device, path, TEMP["lobby"], touch=False)
    pos["lobby"] = lobbyPosition

    # 注單記錄
    recordPosition = deepseaImagePos().universal(device, path, TEMP["record"],  touch=False)
    pos["record"] = recordPosition

    # 注單記錄_取消
    recordcancelPosition = deepseaImagePos().universal(device, path, TEMP["recordcancel"], touch=False)
    pos["recordcancel"] = recordcancelPosition

    # 規則頁
    rulePosition = deepseaImagePos().universal(device, path, TEMP["rule"])
    pos["rule"] = rulePosition

    # 規則頁切換
    ruleswitchPosition = deepseaImagePos().universal(device, path, TEMP["ruleswitch"])
    pos["ruleswitch"] = ruleswitchPosition

    # 規則頁_取消
    rulecancelPosition = deepseaImagePos().universal(device, path, TEMP["rulecancel"])
    pos["rulecancel"] = rulecancelPosition

    # 音樂設定
    settingPosition = deepseaImagePos().universal(device, path, TEMP["musicsetting"])
    pos["musicsetting"] = settingPosition

    # 音樂設定_取消
    settingcancelPosition = deepseaImagePos().universal(device, path, TEMP["settingcancel"])
    pos["settingcancel"] = settingcancelPosition

    # cancel
    cancelPosition = deepseaImagePos().universal(device, path, TEMP["cancel"])
    pos["cancel"] = cancelPosition

    # 未下注警告彈窗
    print("# --------------------------")
    print("等候150秒")
    print("# --------------------------")
    time.sleep(150)
    popoutPosition = deepseaImagePos().universal(device, path, TEMP["popoutalert"], touch=False)
    pos["popout"] = popoutPosition

    # 未下注警告彈窗_確認
    confirmPosition = deepseaImagePos().universal(device, path, TEMP["confirm"])
    pos["confirm"] = confirmPosition

    # spin
    # 旋轉
    spinPosition = deepseaImagePos().universal(device, path, TEMP["spin"])
    pos["spin"] = spinPosition
    
    return pos

# if __name__ == '__main__':
#     import common
#     device = action.deviceConnect()
#     # device = action.deviceRemoteConnect()
#     path = common.folderRemake(mark=True)
#     deepseaFlow(device, path)