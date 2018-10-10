#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.BasePage import BasePage
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class Login_Page(BasePage):
    '''登录页面'''

    @teststep
    def click_login_btn(self):
        self.d(resourceId="com.quvideo.xiaoying:id/btn_v6_login").click()
        self.d(resourceId="com.quvideo.xiaoying:id/login_last_other").click_exists(timeout=2)

    @teststep
    def click_qq(self):
        self.d(resourceId="com.quvideo.xiaoying:id/rl_login_qq").click()
        self.d(resourceId="com.tencent.mobileqq:id/name", text=u"登录").click()


if __name__ == '__main__':
    from Public.Log import Log
    Log().set_logger('udid', './log.log')
    BasePage().set_driver('10.0.29.65')
    Login_Page().click_login_btn()
    Login_Page().click_qq()