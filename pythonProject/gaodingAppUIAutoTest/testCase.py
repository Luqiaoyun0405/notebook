# -*- encoding=utf8 -*-
__author__ = "Administrator"
from airtest.core.api import *
auto_setup( __file__ )
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
class TestCase:
    str1 = "TestCase的属性"
    def __init__(self):
        connect_device("Android:///")  # 连接设备
        start_app( "com.hlg.daydaytobusiness" )
    def switchRatioAndSavePhoto(self):
        poco = AndroidUiautomationPoco( use_airtest_input=True, screenshot_each_action=False )
        sleep( 5 )
        poco( text="图片标记" ).click()
        poco.swipe( [0.5, 0.7], [0.5, 0.3] )
        sleep( 5 )
        poco.click( [0.4, 0.4] )
        poco( text="制作" ).click()
        sleep(2)
        poco( text="编辑" ).click()
        sleep(2)
        poco( text="3:4" ).click()
        poco( text="完成" ).click()
        sleep(2)
        poco( text="保存" ).click()
        sleep(2)
        poco( text="返回首页").click()





case = TestCase()
print( case.str1 )
case.switchRatioAndSavePhoto()

"""
    poco( name="com.hlg.daydaytobusiness:id/tv_search").click()
    text("中秋")
    #poco(name="android.view.View").set_text("")
    text("博饼",search=True)
    """
    #saveText = poco(name="com.hlg.daydaytobusiness:id/save_photo_prompt_words").get_text()
    #print(saveText)
    #assert_equal(poco(name=,"已保存至相册")
    #assert_exists( Template( r"tpl1562829085071.png", record_pos=(0.015, -0.099), resolution=(1080, 2160) ), "切换比例测试" )
