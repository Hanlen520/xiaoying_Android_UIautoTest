#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Public.BasePage import BasePage
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError

class Studio_Page(BasePage):
    @teststep
    def click_item(self,inst=0):
        item = self.d(resourceId="com.quvideo.xiaoying:id/xiaoying_studio_item_layout")
        if item.child(resourceId='com.quvideo.xiaoying:id/xiaoying_studio_layout_left').exists:
