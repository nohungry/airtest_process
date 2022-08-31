import subprocess
import common
import action
import database
import time
import gc

from temp import GameFlow


if __name__ == '__main__':
    status = subprocess.call("adb devices", shell=True)
    assert status == 0, "something is wrong"
    device = action.deviceConnect()
    # resolution = action.phoneResolution()
    path = common.folderRemake(mark=True)
    for _ in range(10):
        # 深海歷險
        deepsea = GameFlow()
        deepseaPos = deepsea.deepsea(device, path)

        # insert進DB步驟
        # dataform = database.value_transfer(device.serialno, deepseaPos)
        # table_name = "deepseaposition"
        # engine, session, metadata = database.connect_DB()
        # ex_table = database.use_table(table_name, metadata, engine)
        # database.insert_value(session, ex_table, dataform)

        # delete process
        del deepsea
        gc.collect()
        time.sleep(30)

    # print(deepseaPos)
    # print("#-----------------")
    # print()
    # for k, v in deepseaPos.items():
    #     print(k, "座標點: ", v)