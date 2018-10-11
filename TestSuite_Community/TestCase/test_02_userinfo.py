#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Public.BasePage import BasePage
from Public.Decorator import *
import unittest

from Public.ReadConfig import ReadConfig
from PageObject import Creation,Camera,Login,Community
from Public.Test_data import *

apk_url = ReadConfig().get_apk_url()
apk = get_apk()
pkg_name = ReadConfig().get_pkg_name()



class Community_UserInfo(unittest.TestCase, BasePage):
    '''社区相关 用户空间测试'''

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
    def test_01_getinfo(self):
        '''可下拉刷新，且个人页数据加载显示正常'''
        Creation.Creation_Page().click_my_btn()
        self.swipe_down(steps=0.05)
        info = str(Community.UserInfo_Page().get_user_info())
        print('name, introduce, id, zan_count, fans_count, follow_count, works_count, likes_count is \n%s' % info)
        self.screenshot()

    @testcase
    def test_02_tab_action(self):
        '''作品 / 喜欢栏可左右滑动或点击tab进行切换'''
        Creation.Creation_Page().click_my_btn()
        # 点击喜欢
        Community.UserInfo_Page().select_tab(2)
        self.assertTrue(Community.UserInfo_Page().is_like_tab())
        # 点击作品
        Community.UserInfo_Page().select_tab(1)
        self.assertFalse(Community.UserInfo_Page().is_like_tab())

        task = self.d(resourceId="com.quvideo.xiaoying:id/recyclerView")
        # 左滑
        self.swipe_left(task, steps=0.02)
        self.assertTrue(Community.UserInfo_Page().is_like_tab())

        # 右滑
        self.swipe_right(task, steps=0.02)
        self.assertFalse(Community.UserInfo_Page().is_like_tab())
        self.screenshot()




if __name__ == '__main__':
    from Public.Log import Log
    Log().set_logger('udid', './log.log')
    BasePage().set_driver('10.0.29.65')
    suite = unittest.TestSuite()
    suite.addTest(Community_UserInfo('test_01_getinfo'))
    suite.addTest(Community_UserInfo('test_02_tab_action'))

    runner = unittest.TextTestRunner()
    runner.run(suite)


