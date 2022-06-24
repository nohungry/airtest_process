from airtest.core.api import *
from airtest.core.api import G
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import connect_device
# import time
# from airtest.core.cv import loop_find, Template
# from airtest.core.settings import Settings as ST


device1 = connect_device("Android:///1576457605007R5?cap_method=&touch_method=adb")
deviceInfo = device()
# 查詢到cap_method是甚麼
# print(device1.cap_method)
# print(deviceInfo.get_display_info())
# apps = deviceInfo.list_app()
# for index in apps:
#     print(index)

# start_app("com.android.chrome")
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# poco("com.android.chrome:id/tab_switcher_button").click()
# poco(name="新增分頁").click()
# poco("com.android.chrome:id/search_box_text").click()
# poco("com.android.chrome:id/url_bar").set_text("http://egame.uat.kk168-01.com/Login")
# # enter按鍵
# keyevent("66")
# poco(text="*帐号").sibling()[1].click()
# text("norman001", enter=False)
# poco(text="*帐号").sibling()[3].click()
# text("000000", enter=False)
# poco(text="登入").click()
# time.sleep(3)
# poco("app").child()[0].child()[0].child()[0].child()[0].child()[1].click()
# touch(Template(r"C:\Users\norman_cheng\Desktop\airtest_project\test001.air\roll.png", record_pos=(-0.003, 0.703), resolution=(1080, 2400)))
# time.sleep(3)
# test = Template(r"C:\Users\norman_cheng\Desktop\airtest_project\test001.air\roll.png")
# touch(Template(r"C:\Users\norman_cheng\Desktop\airtest_project\test001.air\roll.png", resolution=(1080, 2400)))

# pos = loop_find(test)
#
# screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
# match_pos = test.match_in(screen)









