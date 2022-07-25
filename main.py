import common
import action

from temp import GameFlow


if __name__ == '__main__':
    device = action.deviceConnect()
    # device = action.deviceRemoteConnect()
    path = common.folderRemake(mark=True)
    # 深海歷險
    deepsea = GameFlow()
    deepseaPos = deepsea.deepsea(device, path)

    print(deepseaPos)
    
