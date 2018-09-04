#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.BasePage import BasePage
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError


class Creation_Page(BasePage):
    @teststep
    def wait_page(self):
        try:
            if self.d(resourceId="com.quvideo.xiaoying:id/btn_vip").wait(timeout=15):
                pass
            else:
                raise Exception('Not in Creation_Page')
        except Exception:
            raise Exception('Not in Creation_Page')

    @teststep
    def click_vip_btn(self):
        '''点击VIP按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/btn_vip").click()

    @teststep
    def click_ad_btn(self):
        self.d(resourceId="com.quvideo.xiaoying:id/btn_shuffle").click()

    @teststep
    def click_edit_btn(self):
        '''点击编辑按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/btn1").click()

    @teststep
    def click_camera_btn(self):
        '''点击拍摄按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/btn2").click()
        time.sleep(4)  # 等待相机加载完成

    @teststep
    def click_view_pager_btn(self, text):
        '''
        次要功能位置，各个按钮的点击操作
        :param text: 次要功能位置的text名称
        :return:
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/view_pager", scrollable=True).fling.horiz.forward(textContains=text)
        self.d(text=text).click()

        # self.d(resourceId="com.quvideo.xiaoying:id/view_pager", scrollable=True).fling.horiz.toBeginning()
        # time.sleep(0.5)
        # ele = self.d(text=text)
        # if ele.exists:
        #     ele.click()
        # else:
        #     self.d(resourceId="com.quvideo.xiaoying:id/view_pager", scrollable=True).fling.horiz.toEnd()
        #     self.d(text=text).click()

    @teststep
    def click_more_btn(self):
        '''点击更多草稿'''
        self.d(resourceId="com.quvideo.xiaoying:id/btn_more").click()

    @teststep
    def click_studio_view(self, inst=0):
        '''
        点击我的工作室的view 默认第一个
        :param inst: 0为第一个view 以此类推 0\1\2--> 一二三
        '''
        self.d(resourceId="com.quvideo.xiaoying:id/layout_draft_item").child(className='android.widget.ImageView')[inst].click()

    @teststep
    def click_find_btn(self):
        self.d(resourceId="com.quvideo.xiaoying:id/img_find").click()

    @teststep
    def click_creation_btn(self):
        self.d(resourceId="com.quvideo.xiaoying:id/img_creation").click()

    @teststep
    def click_my_btn(self):
        self.d(resourceId="com.quvideo.xiaoying:id/img_studio").click()


if __name__ == '__main__':
    from Public.Log import Log
    Log().set_logger('udid', './log.log')
    BasePage().set_driver('8DAQLNJNR4IZ6H5L')
    Creation_Page().click_view_pager_btn('画中画编辑')

