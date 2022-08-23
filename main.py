import subprocess
import common
import action
import database

from temp import GameFlow


if __name__ == '__main__':
    status = subprocess.call("adb devices", shell=True)
    assert status == 0, "something is wrong"
    device = action.deviceConnect()
    # device = action.deviceRemoteConnect()
    path = common.folderRemake(mark=True)
    # 深海歷險
    deepsea = GameFlow()
    deepseaPos = deepsea.deepsea(device, path)

    print(deepseaPos)
    # print("#-----------------")
    # print()
    # for k, v in deepseaPos.items():
    #     print(k, "座標點: ", v)