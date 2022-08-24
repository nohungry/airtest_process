import subprocess
import common
import action
import database

from temp import GameFlow


if __name__ == '__main__':
    status = subprocess.call("adb devices", shell=True)
    assert status == 0, "something is wrong"
    device = action.deviceConnect()
    # device_num = device.serialno
    # phone resolution
    resolution = action.phoneResolution()
    # device = action.deviceRemoteConnect()
    path = common.folderRemake(mark=True)
    # 深海歷險
    deepsea = GameFlow()
    deepseaPos = deepsea.deepsea(device, path)
    # insert進DB
    dataform = {
        "phoneUDID": device.serialno,
        "spin": deepseaPos["spin"]["result"],
        "spin_weights": deepseaPos["spin"]["confidence"],
        "addition": deepseaPos["addition"]["result"],
        "addition_weights": deepseaPos["addition"]["confidence"],
        "subtraction": deepseaPos["subtraction"]["result"],
        "subtraction_weights": deepseaPos["subtraction"]["confidence"],
        "lighting": deepseaPos["lighting"]["result"],
        "lighting_weights": deepseaPos["lighting"]["confidence"],
        "loop": deepseaPos["loop"]["result"],
        "loop_weights": deepseaPos["loop"]["confidence"],
        "autoloop": deepseaPos["autoloop"]["result"],
        "autoloop_weights": deepseaPos["autoloop"]["confidence"],
        "autostart": deepseaPos["autostart"]["result"],
        "autostart_weights": deepseaPos["autostart"]["confidence"],
        "contents": deepseaPos["contents"]["result"],
        "contents_weights": deepseaPos["contents"]["confidence"],
        "lobby": deepseaPos["lobby"]["result"],
        "lobby_weights": deepseaPos["lobby"]["confidence"],
        "record": deepseaPos["record"]["result"],
        "record_weights": deepseaPos["record"]["confidence"],
        "recordcancel": deepseaPos["recordcancel"]["result"],
        "recordcancel_weights": deepseaPos["recordcancel"]["confidence"],
        "rule": deepseaPos["rule"]["result"],
        "rule_weights": deepseaPos["rule"]["confidence"],
        "ruleswitch": deepseaPos["ruleswitch"]["result"],
        "ruleswitch_weights": deepseaPos["ruleswitch"]["confidence"],
        "rulecancel": deepseaPos["rulecancel"]["result"],
        "rulecancel_weights": deepseaPos["rulecancel"]["confidence"],
        "musicsetting": deepseaPos["musicsetting"]["result"],
        "musicsetting_weights": deepseaPos["musicsetting"]["confidence"],
        "settingcancel": deepseaPos["settingcancel"]["result"],
        "settingcancel_weights": deepseaPos["settingcancel"]["confidence"],
        "cancel": deepseaPos["cancel"]["result"],
        "cancel_weights": deepseaPos["cancel"]["confidence"],
        "popout": deepseaPos["popout"]["result"],
        "popout_weights": deepseaPos["popout"]["confidence"],
        "confirm": deepseaPos["confirm"]["result"],
        "confirm_weights": deepseaPos["confirm"]["confidence"],
    }

    # print(deepseaPos)
    # print("#-----------------")
    # print()
    # for k, v in deepseaPos.items():
    #     print(k, "座標點: ", v)