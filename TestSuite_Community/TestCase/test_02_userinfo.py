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

apk_url = ReadConfig().get_apk_url()
apk = get_apk()
pkg_name = ReadConfig().get_pkg_name()




class community_userinfo(unittest.TestCase, BasePage):
    '''社区相关 用户空间测试'''

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
    def test_01_getinfo(self):
        '''可下拉刷新，且个人页数据加载显示正常 ###查看截图'''
        log.i('个人页下拉刷新')
        creation.creation_page().click_my_btn()
        self.swipe_down(steps=0.1)
        time.sleep(1)
        info = str(community.userinfo_page().get_user_info("title"))
        log.i('userame  is \n%s' % info)
        self.screenshot()

    @testcase
    def test_02_tab_action(self):
        '''作品 / 喜欢栏点击tab进行切换'''
        log.i('作品 / 喜欢栏点击tab进行切换')
        # time.sleep(5)  # 等待debug的 toast消失
        # 点击喜欢
        log.i("click like btn")
        community.userinfo_page().select_tab(2)
        time.sleep(0.5)
        like = community.userinfo_page().is_like_tab()
        self.assertTrue(like)
        # 点击作品
        log.i("click works btn")
        community.userinfo_page().select_tab(1)
        time.sleep(0.5)
        like = community.userinfo_page().is_like_tab()
        self.assertFalse(like)

        '''滑动在不同手机上有点问题 先注释掉'''
        # task = self.d(resourceId="com.quvideo.xiaoying:id/recyclerView")
        # # 左滑
        # log.i("swipe_left")
        # self.swipe_left(task, steps=0.03)
        # time.sleep(0.5)
        # like = community.userinfo_page().is_like_tab()
        # self.assertTrue(like)
        #
        # # 右滑
        # log.i("swipe_rigth")
        # self.swipe_right(task, steps=0.03)
        # time.sleep(0.5)
        # like = community.userinfo_page().is_like_tab()
        # self.assertFalse(like)


    @testcase
    def test_03_back_top(self):
        '''上移页面可收起个人信息栏，点击一键回顶部的按钮，可返回视频列表顶部  ##查看截图'''
        log.i('上移页面可收起个人信息栏，点击一键回顶部的按钮')

        creation.creation_page().click_my_btn()
        for i in range(5):
            BasePage().swipe_up(steps=0.05)
        log.i('点击前截图')
        self.screenshot()
        community.userinfo_page().click_back_top_btn()
        log.i('点击后截图')
        self.screenshot()

    @testcase
    def test_04_click_to_top(self):
        '''点击击我Tab均可返回当前页顶部并刷新 ##查看截图'''
        log.i('点击击我Tab均可返回当前页顶部并刷新')
        creation.creation_page().click_my_btn()
        for i in range(5):
            BasePage().swipe_up(steps=0.05)
        log.i('点击前截图')
        self.screenshot()
        creation.creation_page().click_my_btn()
        log.i('点击后截图')
        self.screenshot()

    @testcase
    def test_05_click_fans_btn(self):
        '''点击获赞数'''
        count = community.userinfo_page().click_zannum_btn()
        log.i(count)

    @testcase
    def test_06_follow(self):
        '''关注列表操作'''
        community.userinfo_page().click_follownum_btn()
        info = community.fans_follow_list_page().get_info()
        community.fans_follow_list_page().click_avatar()
        title = community.userinfo_page().get_user_info()
        log.i('跳转到用户页面判断用户名是否一致')
        self.assertEqual(info[0], title)
        self.back()
        community.fans_follow_list_page().click_follow_btn()
        self.back()
        community.userinfo_page().click_follownum_btn()
        log.i('取消关注后，再次进入到关注也判断之前用户是否存在')
        self.assertIsNot(community.fans_follow_list_page().get_info(), info)

    @testcase
    def test_07_fans(self):
        '''粉丝列表操作'''
        community.userinfo_page().click_fansnum_btn()
        info = community.fans_follow_list_page().get_info()
        log.i(info)
        community.fans_follow_list_page().click_avatar()
        title = community.userinfo_page().get_user_info()
        self.assertEqual(info[0], title)
        self.back()
        community.fans_follow_list_page().click_follow_btn()
        new_info = community.fans_follow_list_page().get_info()
        log.i('点击关注之后的信息：%s' % str(new_info))
        self.assertIsNot(info[2], new_info[2])








if __name__ == '__main__':
    from Public.Log import Log
    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    # d = BasePage().get_driver()
    # d.app_start("com.quvideo.xiaoying")

    suite = unittest.TestSuite()
    suite.addTest(community_userinfo('test_01_getinfo'))
    suite.addTest(community_userinfo('test_01_getinfo'))
    suite.addTest(community_userinfo('test_02_tab_action'))
    suite.addTest(community_userinfo('test_03_back_top'))
    suite.addTest(community_userinfo('test_04_click_to_top'))
    suite.addTest(community_userinfo('test_05_click_fans_btn'))
    suite.addTest(community_userinfo('test_06_follow'))
    suite.addTest(community_userinfo('test_07_fans'))

    runner = unittest.TextTestRunner()
    runner.run(suite)


