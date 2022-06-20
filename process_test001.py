from airtest.core.api import *
from airtest.core.api import G
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import connect_device
import time


device1 = connect_device("Android:///1576457605007R5?cap_method=javacap&touch_method=adb")
deviceInfo = device()
# print(deviceInfo.get_display_info())
# apps = deviceInfo.list_app()
# for index in apps:
#     print(index)

start_app("com.android.chrome")
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco("com.android.chrome:id/tab_switcher_button").click()
poco(name="新增分頁").click()
poco("com.android.chrome:id/search_box_text").click()
poco("com.android.chrome:id/url_bar").set_text("http://egame.uat.kk168-01.com/Login")
# enter按鍵
keyevent("66")
poco(text="*帐号").sibling()[1].click()
text("norman001", enter=False)
poco(text="*帐号").sibling()[3].click()
text("000000", enter=False)
poco(text="登入").click()
time.sleep(3)
poco("app").child()[0].child()[0].child()[0].child()[0].child()[1].click()






