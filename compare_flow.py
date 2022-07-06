from airtest.core.api import *
from airtest.core.api import G
from airtest.core.api import connect_device
from airtest.utils.transform import TargetPos

from airtest.aircv.keypoint_matching_contrib import SIFTMatching
from feature_Re import KAZEMatching

# 手機連接
device1 = connect_device("Android:///1576457605007R5?cap_method=minicap&touch_method=adb")

# windows screen 預處理完成, 轉變為CV2格式
windowsScreen = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_screen\windows_screen.jpg")
screenCV2 = windowsScreen._imread()

# target Image 預處理完成, 轉變為CV2格式
targetImage = Template(r"C:\Users\norman_cheng\Desktop\airtest001\image\windows_target\windows_spin.jpg")
targetCV2 = targetImage._imread()

# 使用aircv內建的SIFT & 重構KAZE作結果比較
sift = SIFTMatching(targetCV2, screenCV2, threshold=0.5)
kaze = KAZEMatching(targetCV2, screenCV2, threshold=0.5)
sift_result = sift.find_best_result()
kaze_result = kaze.find_best_result()
print(sift_result)
print(kaze_result)