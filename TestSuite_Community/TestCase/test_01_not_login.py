#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Public.BasePage import BasePage
from Public.Decorator import *
import unittest

from Public.ReadConfig import ReadConfig
from PageObject import creation, camera, login, community
from Public.Test_data import *

apk_url = ReadConfig().get_apk_url()
apk = get_apk()
pkg_name = ReadConfig().get_pkg_name()

@unittest.skip
class Community_Not_Login(unittest.TestCase, BasePage):
    '''社区相关 账号未登录'''

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

    @unittest.skip
    @testcase
    def test_01_install(self):
        '''小影安装，并允许各种权限'''
        self.d.app_uninstall(pkg_name)
        self.local_install(apk['apk_path'])
        time.sleep(2)
        self.watch_device('允许|始终允许|取消|立即删除')  # 华为删除app后弹出清理弹窗
        self.d.app_start(pkg_name)
        self.d(resourceId="com.quvideo.xiaoying:id/wel_skip").click_exists(timeout=20)
        self.unwatch_device()

        creation.creation_page().click_creation_btn()
        # # 进入gallery
        # Creation.Creation_Page().click_edit_btn()
        # if self.d(resourceId="com.quvideo.xiaoying:id/vip_home_help_dialog_skip").click_exists(timeout=3):
        #     Creation.Creation_Page().click_edit_btn()
        # self.d(resourceId="com.quvideo.xiaoying:id/gallery_chooser_layout").wait()
        # self.back()
        # # 进入camera,允许权限
        # self.watch_device('允许|始终允许|取消')
        # Creation.Creation_Page().click_camera_btn()
        # time.sleep(2)
        # self.back()
        # self.d(text='取消').click_exists(timeout=3)
        # self.unwatch_device()

    @testcase
    def test_02_Jump_login(self):
        '''未登录，评论@、点赞评论、回复评论、转发、关注、私信、拉黑 均应弹出登录框'''
        # '''未登录，点击评论、回复、点赞评论、评论@、关注、转发、拉黑、私信、参加活动、上传、描述@、登录等均应弹出登录框'''
        creation.creation_page().click_find_btn()
        community.community_page().select_Bar(2)
        # 下拉刷新
        self.swipe_down(steps=0.05)
        community.community_page().select_video_thumb()

        # 点击静音按钮以消除引导图
        community.feedVideo_page().click_MuteMode_btn()

        while community.feedVideo_page().get_video_info("comment") == "-":
            self.swipe_up(steps=0.05)
            time.sleep(2)
        community.feedVideo_page().click_comment_btn()
        # 评论@
        community.feedVideo_page().click_at_btn()
        self.assertTrue(login.login_page().is_login_page())
        self.back()
        # 评论点赞
        community.feedVideo_page().commet_lick_btn_click()
        self.assertTrue(login.login_page().is_login_page())
        self.back()
        # 回复评论
        community.feedVideo_page().comment_add()
        self.assertTrue(login.login_page().is_login_page())
        self.back()
        self.back()
        # 转发
        community.feedVideo_page().click_share_btn()
        self.assertTrue(login.login_page().is_login_page())
        self.back()
        # 关注
        if self.d(resourceId="com.quvideo.xiaoying:id/feed_bottom_head_follow_state").exists:
            community.feedVideo_page().click_follow_state()
        else:
            self.swipe_up(steps=0.05)
            time.sleep(2)
            community.feedVideo_page().click_follow_state()
        self.assertTrue(login.login_page().is_login_page())
        self.back()
        # 跳转到他人详情页面
        community.feedVideo_page().click_head_btn()
        # 私信
        community.userinfo_page().select_more_action("私信")
        self.assertTrue(login.login_page().is_login_page())
        self.back()
        # 拉黑
        community.userinfo_page().select_more_action("直接拉黑")
        self.assertTrue(login.login_page().is_login_page())
        self.back()

    @testcase
    def test_03_login(self):
        '''小影账号登录'''
        creation.creation_page().click_my_btn()
        login.login_page().click_login_btn()
        login.login_page().click_qq()
        self.assertTrue(self.d(resourceId="com.quvideo.xiaoying:id/studio_title_text").wait())
        self.screenshot()


if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver('10.0.29.65')
    suite = unittest.TestSuite()
    suite.addTest(Community_Not_Login('test_02_Jump_login'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
