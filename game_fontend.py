from airtest.core.api import *
from airtest.core.api import G
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import connect_device
import time

device1 = connect_device("Android:///1576457605007R5?cap_method=javacap&touch_method=adb")
deviceInfo = device()

# touch(Template())








touch(Template(r"C:\Users\norman_cheng\Desktop\airtest_project\test001.air\roll.png", record_pos=(-0.003, 0.703), resolution=(1080, 2400)))