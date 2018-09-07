#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Public.BasePage import BasePage
from Public.Decorator import *
import unittest

from Public.ReadConfig import ReadConfig
from PageObject import XiaoYingActivity,CameraActivity
from Public.Test_data import *

apk_url = ReadConfig().get_apk_url()
apk = get_apk()
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

    @testcase
    def test_01_install(self):
        '''小影安装，并允许各种权限'''
        self.d.app_uninstall(pkg_name)
        #
        self.local_install(apk['apk_path'])

        # print('install apk from URL：\n%s' % apk_url)
        # self.d.app_install(url=apk_url)

        time.sleep(2)
        self.watch_device(['允许', '始终允许', '取消'])
        self.d.app_start(pkg_name)
        self.d(resourceId="com.quvideo.xiaoying:id/wel_skip").click_exists(timeout=60)
        XiaoYingActivity.Creation_Page().click_creation_btn()



        # XiaoYingActivity.Creation_Page().click_camera_btn()
        # if self.d(resourceId="com.quvideo.xiaoying:id/vip_home_help_dialog_skip").exists:
        #     self.d(resourceId="com.quvideo.xiaoying:id/vip_home_help_dialog_skip").click()
        #     XiaoYingActivity.Creation_Page().click_camera_btn()
        # CameraActivity.Camera_Page().click_record_btn(duration=5)
        # CameraActivity.Camera_Page().click_next_btn()
        # self.d(resourceId="com.quvideo.xiaoying:id/editor_publish").click()
        # # self.d(resourceId="com.quvideo.xiaoying:id/share_btn_share").click()  #
        # # time.sleep(2)
        # self.d(resourceId="com.quvideo.xiaoying:id/layout_draft_btns").click()
        # self.back()
        self.unwatch_device()
        self.screenshot()

    @testcase
    def test_02_click_edit_btn(self):
        '''点击编辑按钮'''
        XiaoYingActivity.Creation_Page().click_creation_btn()
        XiaoYingActivity.Creation_Page().click_edit_btn()
        if self.d(resourceId="com.quvideo.xiaoying:id/vip_home_help_dialog_skip").exists:
            self.d(resourceId="com.quvideo.xiaoying:id/vip_home_help_dialog_skip").click()
            XiaoYingActivity.Creation_Page().click_edit_btn()
        self.d(resourceId="com.quvideo.xiaoying:id/gallery_chooser_layout").wait()
        self.screenshot()
        self.back()

    @testcase
    def test_03_click_camera_btn(self):
        '''点击拍摄按钮'''
        self.watch_device(['允许', '始终允许', '取消'])
        XiaoYingActivity.Creation_Page().click_camera_btn()
        self.screenshot()
        self.back()
        self.back()
        self.d(text='取消').click_exists(timeout=3)
        self.unwatch_device()

    @testcase
    def test_03_click_view_pager_btn(self):
        '''次要功能位的点击操作'''
        # XiaoYingActivity.Creation_Page().click_view_pager_btn('一键大片')  # 不同手机跳转不同
        # time.sleep(2)
        # self.back()
        XiaoYingActivity.Creation_Page().click_view_pager_btn('相册MV')
        self.back()
        XiaoYingActivity.Creation_Page().click_view_pager_btn('美颜趣拍')
        time.sleep(4)
        self.d(text='取消').click_exists(timeout=3)
        self.back()
        XiaoYingActivity.Creation_Page().click_view_pager_btn('素材中心')
        time.sleep(2)
        self.back()
        XiaoYingActivity.Creation_Page().click_view_pager_btn('新手教程')
        time.sleep(2)
        self.back()
        XiaoYingActivity.Creation_Page().click_view_pager_btn('画中画编辑')
        time.sleep(2)
        self.screenshot()
        self.back()

    @testcase
    def test_04_click_studio_view(self):
        '''我的工作室操作'''
        XiaoYingActivity.Creation_Page().click_more_btn()
        self.back()
        XiaoYingActivity.Creation_Page().click_studio_view(1)
        time.sleep(2)
        self.screenshot()




