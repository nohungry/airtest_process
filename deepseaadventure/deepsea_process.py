import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

import action
import procedures
import time

from airtest.utils.transform import TargetPos

from feature_Re import KAZEMatching

DIR_NAME = os.path.dirname(__file__)
TARGET_DIR = os.path.join(DIR_NAME, r"deepsea_target")

TEMP = {
    "spin": os.path.join(TARGET_DIR, r"spin.jpg"),
    "addition": os.path.join(TARGET_DIR, r"addition.jpg"),
    # -----------------------------------------------------------
    "subtraction": os.path.join(TARGET_DIR, r"subtraction.jpg"),
    "subtraction01": os.path.join(TARGET_DIR, r"subtraction01.jpg"),
    "subtraction02": os.path.join(TARGET_DIR, r"subtraction02.jpg"),
    # -----------------------------------------------------------
    "lighting": os.path.join(TARGET_DIR, r"lighting.jpg"),
    "loop": os.path.join(TARGET_DIR, r"loop.jpg"),
    "autoloop": os.path.join(TARGET_DIR, r"autoloop.jpg"),
    "autostart": os.path.join(TARGET_DIR, r"autostart.jpg"),
    "autocancel": os.path.join(TARGET_DIR, r"autocancel.jpg"),
    "contents": os.path.join(TARGET_DIR, r"contents.jpg"),
    "lobby": os.path.join(TARGET_DIR, r"lobby.jpg"),
    "record": os.path.join(TARGET_DIR, r"record.jpg"),
    "recordcancel": os.path.join(TARGET_DIR, r"recordcancel.jpg"),
    "rule": os.path.join(TARGET_DIR, r"rule.jpg"),
    "ruleswitch": os.path.join(TARGET_DIR, r"ruleswitch.jpg"),
    "rulecancel": os.path.join(TARGET_DIR, r"rulecancel.jpg"),
    "musicsetting": os.path.join(TARGET_DIR, r"musicSetting.jpg"),
    "settingcancel": os.path.join(TARGET_DIR, r"settingcancel.jpg"),
    "cancel": os.path.join(TARGET_DIR, r"contents_cancel.jpg"),
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
                return position

            elif match_result == None:
                # raise EOFError("手機當前頁面上沒有找到正確的圖片")
                errortarget = os.path.basename(sign)
                print("手機當前頁面上沒有找到正確的圖片_%s" %errortarget)
                return None
        elif touch == False:
            if match_result != None:
                position = TargetPos().getXY(match_result, 5)
                return position

            elif match_result == None:
                errortarget = os.path.basename(sign)
                print("手機當前頁面上沒有找到正確的圖片_%s" %errortarget)
                return None

def deepseaFlow(device, path):
    # 旋轉
    spinPosition = deepseaImagePos().universal(device, path, TEMP["spin"])
    # 金額"+"
    additionPosition = deepseaImagePos().universal(device, path, TEMP["addition"])
    # 金額"-"
    subtractionPosition = deepseaImagePos().universal(device, path, TEMP["subtraction01"])
    # 快速按鈕(highlight)
    lightingPosition = deepseaImagePos().universal(device, path, TEMP["lighting"])
    # # 取消快速按鈕(no highlight)
    # lightingPosition = deepseaImagePos().universal(device, path, TEMP["lighting"])
    # 循環按鈕
    loopPosition = deepseaImagePos().universal(device, path, TEMP["loop"])
    # 循環設定頁
    autoloopPosition = deepseaImagePos().universal(device, path, TEMP["autoloop"], touch=False)
    # 循環開始
    autostartPosition = deepseaImagePos().universal(device, path, TEMP["autostart"])
    time.sleep(150)
    # # 循環設定頁_取消
    # autocancelPosition = deepseaImagePos().universal(device, path, TEMP["autocancel"])
    # 目錄按鈕
    contentsPosition = deepseaImagePos().universal(device, path, TEMP["contents"])
    # 返回KK大廳
    lobbyPosition = deepseaImagePos().universal(device, path, TEMP["lobby"], touch=False)
    # 注單記錄
    recordPosition = deepseaImagePos().universal(device, path, TEMP["record"])
    # 注單記錄_取消
    recordcancelPosition = deepseaImagePos().universal(device, path, TEMP["recordcancel"])
    # 規則頁
    rulePosition = deepseaImagePos().universal(device, path, TEMP["rule"])
    # 規則頁切換
    ruleswitchPosition = deepseaImagePos().universal(device, path, TEMP["ruleswitch"])
    # 規則頁_取消
    rulecancelPosition = deepseaImagePos().universal(device, path, TEMP["rulecancel"])
    # 音樂設定
    settingPosition = deepseaImagePos().universal(device, path, TEMP["musicsetting"])
    # 音樂設定_取消
    settingcancelPosition = deepseaImagePos().universal(device, path, TEMP["settingcancel"])
    # cancel
    cancelPosition = deepseaImagePos().universal(device, path, TEMP["cancel"])
    


if __name__ == '__main__':
    import common
    device = action.deviceConnect()
    # device = action.deviceRemoteConnect()
    path = common.folderRemake(mark=True)
    deepseaFlow(device, path)