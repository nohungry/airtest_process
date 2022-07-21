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
    "contents": os.path.join(TARGET_DIR, r"contents.jpg"),
    "lobby": os.path.join(TARGET_DIR, r"lobby.jpg"),
    "record": os.path.join(TARGET_DIR, r"record.jpg"),
    "rule": os.path.join(TARGET_DIR, r"rule.jpg"),
    "musicsetting": os.path.join(TARGET_DIR, r"musicSetting.jpg"),
    "cancel": os.path.join(TARGET_DIR, r"contents_cancel.jpg"),
}

class deepseaImagePos(procedures.procedures):
    def universal(self, device, path, sign=None):
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

        if match_result != None:
            position = TargetPos().getXY(match_result, 5)
            device.touch(position)
            time.sleep(5)
            return position

        elif match_result == None:
            # raise EOFError("手機當前頁面上沒有找到正確的圖片")
            print("手機當前頁面上沒有找到正確的圖片_")
            return None
        

def deepseaFlow(device, path):
    # 旋轉
    spinPosition = deepseaImagePos().universal(device, path, TEMP["spin"])
    # 金額"+"
    additionPosition = deepseaImagePos().universal(device, path, TEMP["addition"])
    # 金額"-"
    subtractionPosition = deepseaImagePos().universal(device, path, TEMP["subtraction01"])
    # 快速按鈕
    lightingPosition = deepseaImagePos().universal(device, path, TEMP["lighting"])
    # 循環按鈕
    loopPosition = deepseaImagePos().universal(device, path, TEMP["loop"])
    # 目錄按鈕
    contentsPosition = deepseaImagePos().universal(device, path, TEMP["contents"])
    # 返回KK大廳
    lobbyPosition = deepseaImagePos().universal(device, path, TEMP["lobby"])
    # 注單記錄
    # recordPosition = deepseaImagePos().universal(device, path, TEMP["record"])
    # 規則頁
    # rulePosition = deepseaImagePos().universal(device, path, TEMP["rule"])
    # 音樂設定
    settingPosition = deepseaImagePos().universal(device, path, TEMP["musicsetting"])
    # cancel
    cancelPosition = deepseaImagePos().universal(device, path, TEMP["cancel"])
    


if __name__ == '__main__':
    import common
    device = action.deviceConnect()
    # device = action.deviceRemoteConnect()
    path = common.folderRemake(mark=True)
    deepseaFlow(device, path)