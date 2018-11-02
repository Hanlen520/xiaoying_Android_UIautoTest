#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Public.BasePage import BasePage
from Public.Decorator import *
import unittest

from Public.ReadConfig import ReadConfig
from PageObject import creation,camera,login,gallery
from Public.Test_data import *

apk_url = ReadConfig().get_apk_url()
pkg_name = ReadConfig().get_pkg_name()



class App_install(unittest.TestCase, BasePage):
    '''小影安装测试'''
    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.d.app_stop_all()

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        cls.d.app_stop("com.quvideo.xiaoying")

    @setup
    def setUp(self):
        self.d.app_start(pkg_name)

    @teardown
    def tearDown(self):
        self.d.app_stop(pkg_name)


    @testcase
    def test_01_install(self):
        '''小影安装，并允许各种权限'''
        download_apk()  # 下载小影最新的apk
        apk = get_apk()

        self.d.app_uninstall(pkg_name)
        self.local_install(apk['apk_path'])

        # print('install apk from URL：\n%s' % apk_url)
        # self.d.app_install(url=apk_url)

        time.sleep(2)
        self.watch_device('允许|始终允许|取消|立即删除')   #华为删除app后弹出清理弹窗
        self.d.app_start(pkg_name)
        self.d(resourceId="com.quvideo.xiaoying:id/wel_skip").click_exists(timeout=10)
        self.d(resourceId="com.quvideo.xiaoying:id/imgview_close_btn").click_exists(timeout=5)
        self.unwatch_device()
        creation.creation_page().click_my_btn()
        self.screenshot()

    @testcase
    def test_02_login(self):
        '''小影账号登录后点击编辑按钮'''
        creation.creation_page().click_my_btn()
        login.login_page().click_login_btn()
        login.login_page().click_qq()
        self.assertTrue(self.d(resourceId="com.quvideo.xiaoying:id/studio_title_text").wait())
        print("登录成功")
        # 进入创作页,点击编辑
        creation.creation_page().click_creation_btn()
        while self.d(resourceId="com.quvideo.xiaoying:id/btn_vip").wait(timeout=2):
            creation.creation_page().click_edit_btn()
        # if self.d(resourceId="com.quvideo.xiaoying:id/vip_home_help_dialog_skip").click_exists(timeout=3):
        #     creation.creation_page().click_edit_btn()
        self.assertTrue(self.d(resourceId="com.quvideo.xiaoying:id/gallery_chooser_layout").wait(timeout=5))
        print("打开gallery成功")




    # @testcase
    # def test_03_click_edit_btn(self):
    #     '''点击编辑按钮'''
    #     creation.creation_page().click_creation_btn()
    #     creation.creation_page().click_edit_btn()
    #     if self.d(resourceId="com.quvideo.xiaoying:id/vip_home_help_dialog_skip").click_exists(timeout=3):
    #         creation.creation_page().click_edit_btn()
    #     self.d(resourceId="com.quvideo.xiaoying:id/gallery_chooser_layout").wait()
    #     self.screenshot()


    @testcase
    def test_03_click_camera_btn(self):
        '''点击拍摄按钮'''
        creation.creation_page().click_creation_btn()
        self.watch_device('允许|始终允许|取消')
        creation.creation_page().click_camera_btn()
        self.screenshot()
        self.back()
        self.back()
        self.d(text='取消').click_exists(timeout=3)
        self.unwatch_device()


    @testcase
    def test_04_click_view_pager_btn(self):
        '''次要功能位的点击操作'''
        creation.creation_page().click_creation_btn()
        creation.creation_page().click_view_pager_btn('相册MV')
        self.back()
        creation.creation_page().click_view_pager_btn('美颜趣拍')
        time.sleep(4)
        camera.camera_page().click_close_btn()
        creation.creation_page().click_view_pager_btn('素材中心')
        time.sleep(2)
        self.back()
        creation.creation_page().click_view_pager_btn('画中画编辑')
        time.sleep(2)
        self.screenshot()





if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    suite = unittest.TestSuite()
    suite.addTest(App_install('test_01_install'))
    # suite.addTest(App_install('test_02_login'))
    # suite.addTest(App_install('test_03_click_camera_btn'))
    # suite.addTest(App_install('test_04_click_view_pager_btn'))
    runner = unittest.TextTestRunner()
    runner.run(suite)




