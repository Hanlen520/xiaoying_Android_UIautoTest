#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Public.BasePage import BasePage
from Public.Decorator import *
import unittest

from Public.ReadConfig import ReadConfig
from PageObject import creation,camera,login,community
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
        creation.creation_page().click_my_btn()
        self.swipe_down(steps=0.05)
        info = str(community.userinfo_page().get_user_info("title"))
        print('userame  is \n%s' % info)
        self.screenshot()

    @testcase
    def test_02_tab_action(self):
        '''作品 / 喜欢栏可左右滑动或点击tab进行切换'''
        creation.creation_page().click_my_btn()
        # time.sleep(5)  # 等待debug的 toast消失
        # 点击喜欢
        community.userinfo_page().select_tab(2)
        time.sleep(0.5)
        self.assertTrue(community.userinfo_page().is_like_tab())
        # 点击作品
        community.userinfo_page().select_tab(1)
        time.sleep(0.5)
        self.assertFalse(community.userinfo_page().is_like_tab())

        task = self.d(resourceId="com.quvideo.xiaoying:id/recyclerView")
        # 左滑
        self.swipe_left(task, steps=0.05)
        time.sleep(0.5)
        self.assertTrue(community.userinfo_page().is_like_tab())

        # 右滑
        self.swipe_right(task, steps=0.05)
        time.sleep(0.5)
        self.assertFalse(community.userinfo_page().is_like_tab())
        self.screenshot()

    @testcase
    def test_03_back_top(self):
        '''上移页面可收起个人信息栏，点击一键回顶部的按钮，可返回视频列表顶部'''
        creation.creation_page().click_my_btn()
        for i in range(5):
            BasePage().swipe_up(steps=0.05)
        self.screenshot()
        community.userinfo_page().click_back_top_btn()
        self.screenshot()

    @testcase
    def test_04_doubleclick_to_top(self):
        '''双击我Tab均可返回当前页顶部并刷新；'''
        creation.creation_page().click_my_btn()
        for i in range(5):
            BasePage().swipe_up(steps=0.05)
        self.screenshot()
        creation.creation_page.click_my_btn()
        self.screenshot()





if __name__ == '__main__':
    from Public.Log import Log
    Log().set_logger('udid', './log.log')
    BasePage().set_driver('10.0.29.65')
    # d = BasePage().get_driver()
    # d.app_start("com.quvideo.xiaoying")


    suite = unittest.TestSuite()
    # suite.addTest(Community_UserInfo('test_01_getinfo'))
    suite.addTest(Community_UserInfo('test_02_tab_action'))
    suite.addTest(Community_UserInfo('test_03_back_top'))

    runner = unittest.TextTestRunner()
    runner.run(suite)


