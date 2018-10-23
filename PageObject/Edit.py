#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Public.BasePage import BasePage
from Public.Decorator import *
from uiautomator2 import UiObjectNotFoundError

class Edit_Page(BasePage):
    @teststep
    def select_editor_tab(self, inst=1):
        '''
        切换编辑模块，主题、编辑、效果
        :param inst:1主题；2编辑；3效果
        '''
        self.d(className="android.support.v7.app.ActionBar$b",instance=inst-1).click()

    @teststep
    def click_draft_btn(self):
        '''点击存草稿'''
        self.d(resourceId="com.quvideo.xiaoying:id/editor_draft").click()

    @teststep
    def click_publish_btn(self):
        '''点击发布按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/editor_publish").click()

    @teststep
    def click_back_btn(self):
        '''点击返回按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/editor_back_btn").click()

    @teststep
    def click_seekbar_play_btn(self):
        '''点击播放按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/seekbar_play").click()


    @teststep
    def get_seekabr_time(self):
        '''获取seekbar的播放时长和视频总时长'''
        cur_time = self.d(resourceId="com.quvideo.xiaoying:id/txtview_cur_time").get_text()
        total_time = self.d(resourceId="com.quvideo.xiaoying:id/txtview_duration").get_text()
        return cur_time, total_time

    @teststep
    def select_seelbar_position(self, inst=5):
        '''
        点击seekbar的播放位置
        :param inst: inst  [0~10)之间任意数字  exp 0.2、0.4、...1.8、2.0
        '''
        bar = self.d(resourceId="com.quvideo.xiaoying:id/seekbar_simple_edit").info['bounds']
        y = bar['top'] + (bar['bottom'] - bar['top']) / 2
        unit = (bar['right'] - bar['left']) / 10
        x = bar['left'] + inst * unit
        self.d.long_click(x, y)

    @teststep
    def click_add_clip_bt(self):
        '''点击添加clip按钮'''
        self.d(resourceId="com.quvideo.xiaoying:id/clipedit_add_btn").click()

    @teststep
    ''''''

    @teststep
    def





if __name__ == '__main__':
    from Public.Log import Log

    Log().set_logger('udid', './log.log')
    BasePage().set_driver('10.0.29.65')
    Edit_Page().select_seelbar_position(0.1)
