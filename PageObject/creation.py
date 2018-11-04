#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Public.BasePage import BasePage
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError
from Public.Log import Log
log = Log()

class creation_page(BasePage):
    '''创作页首页'''
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
        log.i('点击VIP按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_vip").click()

    @teststep
    def click_ad_btn(self):
        log.i('点击广告按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_shuffle").click()

    @teststep
    def click_edit_btn(self):
        log.i('点击编辑按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/btn1").long_click()

    @teststep
    def click_camera_btn(self):
        log.i('点击拍摄按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/btn2").click()
        time.sleep(4)  # 等待相机加载完成

    @teststep
    def click_view_pager_btn(self, text):
        '''
        次要功能位置，各个按钮的点击操作
        :param text: 次要功能位置的text名称
        :return:
        '''
        log.i('查找次要功能位 %s 并进行点击操作'% text)
        if self.d(text=text).wait(timeout=1):
            self.d(text=text).click()
            return True
        else:
            try:
                self.d(resourceId="com.quvideo.xiaoying:id/view_pager", scrollable=True).scroll.horiz.to(text=text)
                self.d(text=text).click()
                return True
            except UiObjectNotFoundError:
                print("找不到控件-->%s" % text)
                return False

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
        log.i('点击更多草稿')
        self.d(resourceId="com.quvideo.xiaoying:id/btn_more").click()

    @teststep
    def select_studio_view(self, inst=1):
        '''
        点击我的工作室的view 默认第一个
        :param inst: 0为第一个view 以此类推 1、2、3--> 一二三
        '''
        log.i('点击我的工作室第%s个草稿')
        self.d(resourceId="com.quvideo.xiaoying:id/layout_draft_item").child(className='android.widget.ImageView')[inst-1].click()

    @teststep
    def click_find_btn(self):
        log.i('点击小影圈')
        self.d(resourceId="com.quvideo.xiaoying:id/img_find").click()
        time.sleep(1)

    @teststep
    def click_creation_btn(self):
        log.i('点击创作按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/img_creation").click()
        time.sleep(1)

    @teststep
    def click_my_btn(self):
        log('点击我的按钮')
        self.d(resourceId="com.quvideo.xiaoying:id/img_studio").click()
        time.sleep(1)


if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver(None)
    print(creation_page().click_view_pager_btn('素材中心'))

