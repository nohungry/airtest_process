import os
import shutil

DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop") + "\\"

def folderRemake(mark=False):
    screenFolderPath = os.path.join(DESKTOP, r"snapshot_log")
    if mark == True:
        if os.path.isdir(screenFolderPath):
            try:
                shutil.rmtree(screenFolderPath)
            except OSError as e:
                print(e)
            os.mkdir(screenFolderPath)
        else:
            os.mkdir(screenFolderPath)

        return screenFolderPath

    elif mark == False:
        return screenFolderPath

    else:
        raise ValueError("mark參數應為boolean type")



