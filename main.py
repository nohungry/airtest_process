import subprocess
import common
import action
import database
import time

from temp import GameFlow


if __name__ == '__main__':
    # for _ in range(10):
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
    dataform = database.value_transfer(device.serialno, deepseaPos)
    table_name = "deepseaposition"
    engine, session, metadata = database.connect_DB()
    ex_table = database.use_table(table_name, metadata, engine)
    database.insert_value(session, ex_table, dataform)
    time.sleep(30)

    # print(deepseaPos)
    # print("#-----------------")
    # print()
    # for k, v in deepseaPos.items():
    #     print(k, "座標點: ", v)