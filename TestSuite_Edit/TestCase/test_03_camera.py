#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Public.BasePage import BasePage
from Public.Decorator import *
import unittest

from Public.ReadConfig import ReadConfig
from PageObject import creation,camera,login,community
from Public.Test_data import *
from Public.Log import Log
log = Log()

pkg_name = ReadConfig().get_pkg_name()


class camera_testsuite(unittest.TestCase, BasePage):
    '''相机相关的测试'''

    # @classmethod
    # @setupclass
    # def setUpClass(cls):
    #     cls.d.app_stop_all()
    #
    # @classmethod
    # @teardownclass
    # def tearDownClass(cls):
    #     cls.d.app_stop("com.quvideo.xiaoying")
    #
    @setup
    def setUp(self):
        self.d.app_start(pkg_name)

    @teardown
    def tearDown(self):
        self.d.app_stop(pkg_name)

    @testcase
    def test_01_click_camera_btn(self):
        '''高清相机进入并退出操作'''
        creation.creation_page().click_creation_btn()
        self.watch_device('允许|始终允许|取消')
        creation.creation_page().click_camera_btn()
        self.screenshot()
        self.back()
        self.d(text='取消').click_exists(timeout=3)
        self.unwatch_device()

    @testcase
    def test_02_camera_ratio(self):
        '''切换相机比例'''
        creation.creation_page().click_camera_btn()
        self.screenshot()
        camera.camera_page().click_cam_ratio_btn()
        print('切换相机比例并截图')
        self.screenshot()
        camera.camera_page().click_cam_ratio_btn()
        print('再次切换相机比例并截图')
        self.screenshot()
        camera.camera_page().click_cam_ratio_btn()

    @testcase
    def test_03_camera_change(self):
        '''前后摄像头切换'''
        creation.creation_page().click_camera_btn()
        camera.camera_page().click_cam_switch_btn()
        print('切换相机到前置摄像头并截图')
        self.screenshot()
        camera.camera_page().click_cam_switch_btn()
        print('切换回到后摄像头并截图')
        self.screenshot()

    @testcase
    def test_04_camera_setting(self):
        '''相机设置'''
        creation.creation_page().click_camera_btn()
        camera.camera_page().click_cam_setting_btn()
        camera.camerasetting_page().switch_flashlight()
        print('打开闪光灯')
        self.screenshot()
        camera.camerasetting_page().switch_flashlight()

        camera.camerasetting_page().switch_grid()
        print('设置九宫格')
        self.screenshot()

        camera.camerasetting_page().select_record_speed(2)
        print('设置拍摄速度')
        self.screenshot()
        camera.camerasetting_page().select_countdown_time()
        print('设置倒计时')
        self.screenshot()
        camera.camerasetting_page().switch_aelock()
        self.back()
        tips = camera.camera_page().get_aelock_tip()
        print(tips)
        self.screenshot()

        camera.camera_page().click_record_btn()
        time.sleep(2)
        print('点击录制后1秒 截图查看倒计时')
        self.screenshot()















